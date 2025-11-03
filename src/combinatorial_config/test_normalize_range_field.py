import unittest
from combinatorial_config.normalize_range_field import normalize_range_field


class TestNormalizeRangeField(unittest.TestCase):
    def test_single_value(self):
        self.assertEqual(normalize_range_field((3,)), (0, 3, 1))

    def test_two_values(self):
        self.assertEqual(normalize_range_field((2, 5)), (2, 5, 1))

    def test_three_values(self):
        self.assertEqual(normalize_range_field((1, 10, 2)), (1, 10, 2))

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            normalize_range_field(("a",))
        with self.assertRaises(ValueError):
            normalize_range_field((1, "b"))
        with self.assertRaises(ValueError):
            normalize_range_field((1, 2, 3, 4))
        with self.assertRaises(ValueError):
            normalize_range_field([])  # not a tuple


if __name__ == "__main__":
    unittest.main()
