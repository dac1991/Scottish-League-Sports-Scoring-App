import unittest
from models.league import League

class TestLeague(unittest.TestCase):
    
    def setUp(self):
        self.league = League("Scottish Premier League", 4)
        self.league.league_teams = ["Team1", "Team2", "Team3", "Team4" ]
        
    def test_league_has_name(self):
        self.assertEqual("Scottish Premier League", self.league.league_name)

    def test_league_has_correct_number_of_competitors(self):
        self.assertEqual(5, len(self.league.league_teams))

    def test_league_has_too_few_teams(self):
        self.league_too_few_teams = League("Null and Void", 12)
        self.assertEqual(False, self.league_too_few_teams.check_correct_number_of_teams_for_league_size())
        
    def test_league_has_too_many_teams(self):
        self.league_too_many_teams = League("Null and Void", 3)
        self.assertEqual(False, self.league_too_many_teams.check_correct_number_of_teams_for_league_size())