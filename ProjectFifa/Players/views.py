from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from Players.models import *
from django.db.models import Q, Avg
from Players.static.Players import Logic
from .forms import ClubForm


def search_players(request, request_year=2021):
    if request.method == "GET":
        searched_player = request.GET.get('get_request_player')
        players = FactPlayerstats.objects.filter(sofifa_id__short_name__icontains=searched_player, year=request_year)
        context = {'searched_player':searched_player, 'players':players, 'request_year':request_year}
        return render(request, 'Players/searched_players.html', context)
    else:
        players = FactPlayerstats.objects.filter(year=request_year)
        context = {'players':players}
        return render(request, 'Players/homepage.html', context)


def homepage(request, request_year=2021):
    year = DimYear.objects.all()
    players = FactPlayerstats.objects.filter(year=request_year)

    if request.method == 'GET':
        if request.GET.get('get_request_year',''):
            request_year = request.GET.get('get_request_year','')
            return HttpResponseRedirect(reverse('Players:homepage', args=(request_year,)))

    page_obj = Logic.generic_paginator(request, players, 15)

    context = {'players': players, 'year': year, 'request_year': request_year, 'page_obj': page_obj}
    return render(request, 'Players/homepage.html', context)

#Refactor
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
    #clubname to filter the players and year
    clubname = club.club_name

    #aggregates the score for the team
    from django.db.models import Func
    class Round_club_avg(Func):
        function = "ROUND"
        template = "%(function)s(%(expressions)s::numeric, 0)"
    aggregate_scores = DimPositioncategory.objects.annotate(num_players = Round_club_avg(Avg('dimpositions__factplayerstats__overall', filter=Q(dimpositions__factplayerstats__club_name= clubname)&Q(dimpositions__factplayerstats__year=request_year)))).filter(~Q(position_categoryid = 3))

    #gets players of a particular club for a given year
    players = FactPlayerstats.objects.filter(club_name = clubname, year = request_year).order_by('positionid__position_categoryid')
    #gets all years that club existed
    year = FactPlayerstats.objects.filter(club_name = clubname).values('year').distinct()

    context = {'club':club,'aggregate_scores': aggregate_scores,'clubname': clubname, 'players': players, 'year': year, 'request_year': request_year}
    return render(request, 'Players/club_detail.html', context)


def club_edit(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)

        if form.is_valid():
            latestid = DimClubs.objects.latest('clubid').clubid
            club_name = form.cleaned_data['club_name']
            leagueid = form.cleaned_data['leagueid']
            c = DimClubs(clubid= latestid+1, club_name = club_name, leagueid = DimLeagues.objects.get(leagueid=leagueid))
            c.save()
            return HttpResponse("Thanks")
    else:
        form = ClubForm()
        context = {'form': form}
        return render(request,'Players/club_edit.html',context)




