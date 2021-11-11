from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from Players.models import *
from django.db.models import Q, Avg, Count, Sum
from django.db import connection
from Players.static.Players import Logic
from .forms import ClubForm


def homepage(request, query='', request_year=2021):
    year = DimYear.objects.all()
    if query:
        print('phase1')
        print(query)
        players = FactPlayerstats.objects.filter(sofifa_id__short_name__icontains=query, year=request_year)
    else:
        print('phase2')
        players = FactPlayerstats.objects.filter(year=request_year)

    if request.method == 'GET':
        if request.GET.get('get_request_player',''):
            print('phase3')
            query = request.GET.get('get_request_player','')
            return HttpResponseRedirect(reverse('Players:homepage', args=(request_year, query)))
        elif request.GET.get('get_request_year',''):
            request_year = request.GET.get('get_request_year','')
            print(request_year)
            print('query if exists:' + query)
            if query:
                print('phase4')
                return HttpResponseRedirect(reverse('Players:homepage', args=(request_year, query)))
            else:
                print('phase5')
                return HttpResponseRedirect(reverse('Players:homepage', args=(request_year,)))

    page_obj = Logic.generic_paginator(request, players, 15)

    context = {'players': players, 'year': year, 'request_year': request_year,'query':query, 'page_obj': page_obj}
    return render(request, 'Players/homepage.html', context)


def clubs(request, query='', request_year=2021):
    year = DimYear.objects.all() #To show in dropdownlist
    if query:
        print(1)
        print(query)
        Clubstats = Logic.clubpositionaveragewithquery(request_year, query)
    else:
        print(2)
        Clubstats = Logic.clubpositionaverage(request_year)

    if request.method == 'GET': 
        if request.GET.get('get_request_club',''):
            print(3)
            query = request.GET.get('get_request_club','')
            return HttpResponseRedirect(reverse('Players:clubs', args=(request_year,query)))
    
        elif request.GET.get('get_request_year',''):
            request_year = request.GET.get('get_request_year','')
            print(request_year)
            print(query)
            if query:
                print(4)
                return HttpResponseRedirect(reverse('Players:clubs', args=(request_year,query)))
            else:
                print(5)
                return HttpResponseRedirect(reverse('Players:clubs', args=(request_year,)))

    #add exception clause here then remove the null?
    
    page_obj = Logic.generic_paginator(request, Clubstats, 15)

    context = {'Clubstats': Clubstats, 'year': year, 'request_year': request_year, 'page_obj': page_obj}
    return render(request, 'Players/clubs.html', context)


def player_detail(request, player_id, request_year=2021):
    player = FactPlayerstats.objects.get(year= request_year, sofifa_id= player_id)
    year = FactPlayerstats.objects.filter(sofifa_id= player_id).values('year')
    context = {'player':player, 'year': year, 'request_year': request_year}
    return render(request, 'Players/player_detail.html', context)


def club_detail(request, request_club_id, request_year):
    club = DimClubs.objects.get(clubid=request_club_id)
    clubname = club.club_name

    from django.db.models import Func
    class Round_club_avg(Func):
        function = "ROUND"
        template = "%(function)s(%(expressions)s::numeric, 0)"
    aggregate_scores = DimPositioncategory.objects.annotate(num_players = Round_club_avg(Avg('dimpositions__factplayerstats__overall', filter=Q(dimpositions__factplayerstats__club_name= clubname)&Q(dimpositions__factplayerstats__year=request_year)))).filter(~Q(position_categoryid = 3))

    players = FactPlayerstats.objects.filter(club_name = clubname, year = request_year).order_by('positionid__position_categoryid')
    year = FactPlayerstats.objects.filter(club_name = clubname).values('year').distinct()

    context = {'club':club,'aggregate_scores': aggregate_scores,'clubname': clubname, 'players': players, 'year': year, 'request_year': request_year}
    return render(request, 'Players/club_detail.html', context)

def club_edit(request):
    print('heyy')
    if request.method == 'POST':
        form = ClubForm(request.POST)

        if form.is_valid():
            latestid = DimClubs.objects.latest('clubid').clubid
            club_name = form.cleaned_data['club_name']
            leagueid = form.cleaned_data['leagueid']
            print(latestid)
            c = DimClubs(clubid= latestid+1, club_name = club_name, leagueid = DimLeagues.objects.get(leagueid=leagueid))
            c.save()
            return HttpResponse("Thanks")
    else:
        print('phase 1')
        form = ClubForm()
        context = {'form': form}
        return render(request,'Players/club_edit.html',context)




