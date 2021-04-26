import unittest
from models.match import match

class Testmatch(unittest.TestCase):
    def setUp(self):
        self.match = Match(1, 2, "01-01-2021", None, 1)
        self.match_with_result = Match(1, 2, "01-01-2021", "3-0", 1)
    
    def test_match_has_home_team_id(self):
        self.assertEqual(1, self.match.home_team_id)
    
    def test_match_has_away_team_id(self):
        self.assertEqual(2, self.match.away_team_id)

    def test_match_has_date(self):
        self.assertEqual("01-01-2021", self.match.match_date)

    def test_match_has_result(self):
        self.assertEqual("3-0", self.match_with_result.match_result)

    def test_match_has_no_result(self):
        self.assertEqual(None, self.match.match_result)

    def test_match_has_league_id(self):
        self.assertEqual(1, self.match.league_id)
