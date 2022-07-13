import unittest
from functions import user_won, user_lost, user_tied, calculate_user_win_rate

class TestUserGameResult(unittest.TestCase):
    def test_user_won(self):
        self.assertEqual(True, user_won(0, 2))
        self.assertEqual(True, user_won(1, 0))
        self.assertEqual(True, user_won(2, 1))
        self.assertEqual(False, user_won(2, 2))

    def test_user_lost(self):
        self.assertEqual(True, user_lost(1, 2))
        self.assertEqual(True, user_lost(0, 1))
        self.assertEqual(True, user_lost(2, 0))
        self.assertEqual(False, user_lost(2, 2))

    def test_user_tied(self):
        self.assertEqual(True, user_tied(0, 0))
        self.assertEqual(True, user_tied(1, 1))
        self.assertEqual(True, user_tied(2, 2))
        self.assertEqual(False, user_tied(0, 1))

class TestCalculateUserWinRate(unittest.TestCase):
    def test_calculate_user_win_rate(self):
        self.assertEqual(50, calculate_user_win_rate(10, 5, 0))
        self.assertEqual(100, calculate_user_win_rate(13, 10, 3))
        self.assertEqual(0, calculate_user_win_rate(5, 0, 1))
        self.assertEqual(0, calculate_user_win_rate(0, 0, 0))

if __name__ == '__main__':
    unittest.main()
