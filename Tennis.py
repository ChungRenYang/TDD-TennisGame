import unittest
import os
import sys

class Tennis:
    def __init__(self):
        self.score_a = 0
        self.score_b = 0
        self.score_map = { 0: "Love", 1: "Fifften", 2:"Thirty" }
    def player_a_score(self):
        self.score_a += 1
    def player_b_score(self):
        self.score_b += 1
    def getScore(self):
        if self.score_a == self.score_b:    # equal
            if self.score_a < 3:
                return self.score_map[self.score_a] + " All"
            else:
                return "Deuce"
        else:                               # not equal
            if self.score_a < 3 and self.score_b < 3:
                return self.score_map[self.score_a] + " " + self.score_map[self.score_b];
            else:
                diff = self.score_a - self.score_b
                if diff == 1:
                    return "A Adv"
                elif diff == -1:
                    return "B Adv"
                elif diff >= 2:
                    return "A Win"
                elif diff <= -2:
                    return "B Win"

class TennisTest(unittest.TestCase):
    def test_love_all(self):
        tennis = Tennis()
        self.assertEqual("Love All", tennis.getScore())
    def test_fiften_love(self):
        tennis = Tennis()
        tennis.player_a_score()
        self.assertEqual("Fifften Love", tennis.getScore())
    def test_thirty_love(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_a_score()
        self.assertEqual("Thirty Love", tennis.getScore())
    def test_love_fiften(self):
        tennis = Tennis()
        tennis.player_b_score()
        self.assertEqual("Love Fifften", tennis.getScore())
    def test_love_thirty(self):
        tennis = Tennis()
        tennis.player_b_score()
        tennis.player_b_score()
        self.assertEqual("Love Thirty", tennis.getScore())
    def test_fifften_all(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        self.assertEqual("Fifften All", tennis.getScore())
    def test_thirty_all(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        self.assertEqual("Thirty All", tennis.getScore())
    def test_deuce(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        self.assertEqual("Deuce", tennis.getScore())
    def test_adv_a(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        self.assertEqual("A Adv", tennis.getScore())
    def test_adv_b(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_b_score()
        self.assertEqual("B Adv", tennis.getScore())
    def test_a_win(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_a_score()
        self.assertEqual("A Win", tennis.getScore())
    def test_b_win(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_a_score()
        tennis.player_b_score()
        tennis.player_b_score()
        tennis.player_b_score()
        self.assertEqual("B Win", tennis.getScore())
    def test_a_win_4_0(self):
        tennis = Tennis()
        tennis.player_a_score()
        tennis.player_a_score()
        tennis.player_a_score()
        tennis.player_a_score()
        self.assertEqual("A Win", tennis.getScore())
        
if __name__ == '__main__':
    unittest.main()
