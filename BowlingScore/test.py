import unittest
from main import compute_bowling_score

class TestBowlingScore(unittest.TestCase):

    def test_no_skittle(self):
        self.assertEqual(compute_bowling_score([]),0)

    def test_one_skittle(self):
        self.assertEqual(compute_bowling_score([5]),5)

    def test_multiple_skittle(self):
        self.assertEqual(compute_bowling_score([5,3,2,5,4,5]),24)

    def test_spare(self):
        self.assertEqual(compute_bowling_score([5,5,2]),14)

    def test_multiple_spare(self):
        self.assertEqual(compute_bowling_score([5,5,2,8,5]),32)

    def test_strike(self):
        self.assertEqual(compute_bowling_score([10,5,2]),24)

    def test_multi_strike(self):
        self.assertEqual(compute_bowling_score([10,10,10,10]),90)

if __name__ == "__main__":
    unittest.main()