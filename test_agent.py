import unittest
from agent import review_signal


class SignalTests(unittest.TestCase):
    def test_insufficient_data_abstains(self):
        result = review_signal([1, 2, 3])
        self.assertEqual(result["signal"], "insufficient-data")
        self.assertTrue(result["human_review_required"])


if __name__ == "__main__":
    unittest.main()
