from django.test import TestCase
from Players.models import DimPlayers, FactPlayerstats, DimPositions, DimPositioncategory
from ProjectFifa.Players.models import DimClubs
from django.db.models import Q, Avg

from ProjectFifa.ProjectFifa.settings import MIDDLEWARE

# Create your tests here.


class correctplayerandyear(TestCase):

    def setUp(self):
        DimPlayers.objects.create(sofifa_id=123, short_name= 'Cristiano Ronaldo', long_name = 'fifjskjfks', dob='1990-10-10')
        FactPlayerstats.objects.create(sofifa_id=123, year= 2016)
    

    def test_player_is_ronaldo_and_year_is_2016(self):
        #Checks if the correct player and correct year is filtered
        query = 'Cristiano Ronaldo'
        request_year = 2015
        player = FactPlayerstats.objects.filter(sofifa_id__short_name__icontains=query, year=request_year)
        ronaldo = player[0].sofifa_id.short_name
        year = player[0].year
        self.assertEqual(ronaldo, 'Cristiano Ronaldo')
        self.assertEqual(year, 2015)


class correctclub(TestCase):
    #Checks to see if the correct club is selected
    def setUp(self):
        DimClubs.objects.create(clubid=1, club_name='London United', leagueid=1)
    
    def test_club_is_london_year(self):
        query = 'London United'
        club = DimClubs.objects.get(clubid=1)

class correctclubstats(TestCase):
    #Checks to see if the correct stats are calculated
    def setUp(self):
        DimClubs.objects.create(clubid=1, club_name="London United", leagueid=1)
        DimPositions.objects.create(positionid=1, position="ST", position_categoryid=1)
        DimPositions.objects.create(positionid=2, position="LW", position_categoryid=1)
        DimPositions.objects.create(positionid=3, position="CM", position_categoryid=2)
        DimPositions.objects.create(positionid=4, position="DM", position_categoryid=2)
        DimPositions.objects.create(positionid=5, position="CB", position_categoryid=3)
        DimPositions.objects.create(positionid=6, position="GK", position_categoryid=3)
        DimPositions.objects.create(positionid=7, position="SUB", position_categoryid=4)
        DimPositions.objects.create(positionid=8, position="RES", position_categoryid=4)
        DimPositioncategory.objects.create(position_category="ATT", position_categoryid=1)
        DimPositioncategory.objects.create(position_category="MID", position_categoryid=2)
        DimPositioncategory.objects.create(position_category="DEF", position_categoryid=3)
        DimPositioncategory.objects.create(position_category="NONE", position_categoryid=4)
        FactPlayerstats.objects.create(sofifa_id=1, club_name='London United', positionid=1, overall= 50, year=2021)
        FactPlayerstats.objects.create(sofifa_id=2, club_name='London United', positionid=2, overall= 20, year=2021)
        FactPlayerstats.objects.create(sofifa_id=3, club_name='London United', positionid=3, overall= 30, year=2021)
        FactPlayerstats.objects.create(sofifa_id=4, club_name='London United', positionid=4, overall= 70, year=2021)
        FactPlayerstats.objects.create(sofifa_id=5, club_name='London United', positionid=5, overall= 90, year=2021)
        FactPlayerstats.objects.create(sofifa_id=6, club_name='London United', positionid=6, overall= 25, year=2021)
    
    def test_if_clubstats_is_correct(self):
        clubname = "London United"
        request_year = 2021
        #Check if the stats of ATT MID DEF is calculated correctly
        from django.db.models import Func
        class Round_club_avg(Func):
            function = "ROUND"
            template = "%(function)s(%(expressions)s::numeric, 0)"
        aggregate_scores = DimPositioncategory.objects.annotate(num_players = Round_club_avg(Avg('dimpositions__factplayerstats__overall', filter=Q(dimpositions__factplayerstats__club_name= clubname)&Q(dimpositions__factplayerstats__year=request_year)))).filter(~Q(position_categoryid = 3))
        ATT = aggregate_scores[0].position_category
        MID = aggregate_scores[1].position_category
        DEF = aggregate_scores[2].position_category
        self.assertEqual(ATT, 35)
        self.assertEqual(MID, 50)
        #true value is 57.5 but rounds up to 60
        self.assertEqual(DEF, 60)