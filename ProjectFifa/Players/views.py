from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from Players.models import *
from django.db.models import Q, Avg, Count, Sum
from django.db import connection
from Players.static.Players import Logic


def homepage(request, request_year=2021):
    year = DimYear.objects.all()
    players = FactPlayerstats.objects.filter(year=request_year)[:40]

    query = request.GET.get('q','')
    if query == '':
        players = FactPlayerstats.objects.filter(year=request_year)[:40]
    else:
        players = FactPlayerstats.objects.filter(sofifa_id__short_name__icontains=query, year=request_year)[:40]
        print('Not empty')
        print(query)

    context = {'players': players, 'year': year, 'request_year': request_year}
    return render(request, 'Players/homepage.html', context)


def homepage_added(request):
        
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            WITH latest_players AS (
            SELECT
            *
            FROM public."Fact.PlayerStats" AS FP
            WHERE year = 2021
            ), old_players AS (
            SELECT
            Sofifa_id
            FROM public."Fact.PlayerStats"
            WHERE year <> 2021
            )
            SELECT
            *
            FROM latest_players AS LP
            LEFT JOIN public."Dim.Players" AS DP ON LP.Sofifa_id = DP.Sofifa_id
            WHERE LP.Sofifa_id NOT IN (SELECT Sofifa_id FROM old_players)
            '''
        )
        #row = cursor.fetchall()
        #row = list(row[0])
        columns = [col[0] for col in cursor.description]
        fetched = cursor.fetchall()
        row = [
            dict(zip(columns, row))
            for row in fetched
            ]

    context = {'players': row[:40]}
    return render(request, 'Players/homepage_added.html', context)


def homepage_free(request):
    players = FactPlayerstats.objects.filter(club_name__isnull=True)[:40]
    context = {'players':players}
    return render(request, 'Players/free.html', context)


def homepage_loaned(request):
    players = FactPlayerstats.objects.filter(loaned_from__isnull=False)[:40]
    context = {'players':players}
    return render(request, 'Players/loaned.html', context)


def homepage_added(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            WITH oneyearplayers AS 
            (
            SELECT sofifa_id
            FROM public."Fact.PlayerStats"
            GROUP BY sofifa_id
            HAVING count(year) = 1
            )

            SELECT *
            FROM public."Fact.PlayerStats" AS FP
            INNER JOIN oneyearplayers AS OP ON FP.Sofifa_id = OP.Sofifa_id
            WHERE year = 2021
            '''
        )
        #row = cursor.fetchall()
        #row = list(row[0])
        columns = [col[0] for col in cursor.description]
        fetched = cursor.fetchall()
        row = [
            dict(zip(columns, row))
            for row in fetched
            ]
    latestyear = FactPlayerstats.objects.filter(year=2021)
    oldyears = FactPlayerstats.objects.values_list('sofifa_id').exclude(year=2021)
    filteredplayers = latestyear.exclude(sofifa_id__in = oldyears).count()
    context = {'players': row[:40],'oldyears': filteredplayers}
    return render(request, 'Players/added.html', context)


def clubs(request, query='', request_year=2021):
    year = DimYear.objects.all() #To show in dropdownlist
    if query:
        Clubstats = Logic.clubpositionaveragewithquery(request_year, query)
    else:
        Clubstats = Logic.clubpositionaverage(request_year)

    if request.method == 'GET': 
        if request.GET.get('get_request_club',''):
            query = request.GET.get('get_request_club','')
            Clubstats = Logic.clubpositionaveragewithquery(request_year, query)
            print('phase 1')
            print(request_year)
            print(query)
            return HttpResponseRedirect(reverse('Players:clubs', args=(request_year,query)))
    
        elif request.GET.get('get_request_year',''):
            request_year = request.GET.get('get_request_year','')
            if query:
                Clubstats = Logic.clubpositionaveragewithquery(request_year, query)
                return HttpResponseRedirect(reverse('Players:clubs', args=(request_year,query)))
            else:
                Clubstats = Logic.clubpositionaverage(request_year)
                return HttpResponseRedirect(reverse('Players:clubs', args=(request_year,)))

    #add exception clause here then remove the null?
    


    context = {'Clubstats': Clubstats, 'year': year, 'request_year': request_year, 'query':query}
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