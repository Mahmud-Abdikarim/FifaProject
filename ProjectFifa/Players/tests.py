from django.test import TestCase
from Players.models import DimPlayers, FactPlayerstats

# Create your tests here.



class correctplayerandyear(TestCase):

    def setUp(self):
        DimPlayers.objects.create(sofifa_id=123, short_name= 'Cristiano Ronaldo', long_name = 'fifjskjfks', dob='1990-10-10')
        FactPlayerstats.objects.create(sofifa_id=123, year= 2016)
    

    def test_player_is_ronaldo_and_year_is_2016(self):
        "Checks if the correct player and correct year is filtered"
        query = 'Cristiano Ronaldo'
        request_year = 2015
        player = FactPlayerstats.objects.filter(sofifa_id__short_name__icontains=query, year=request_year)
        ronaldo = player[0].sofifa_id.short_name
        year = player[0].year
        self.assertEqual(ronaldo, 'Cristiano Ronaldo')
        self.assertEqual(year, 2015)

