"""Tests for range field normalization."""

import pytest
from combinatorial_config.normalizers import normalize_range_field, range_field_to_list


class TestNormalizeRangeField:
    def test_single_value(self):
        assert normalize_range_field((3,)) == (0, 3, 1)

    def test_two_values(self):
        assert normalize_range_field((2, 5)) == (2, 5, 1)

    def test_three_values(self):
        assert normalize_range_field((1, 10, 2)) == (1, 10, 2)

    def test_float_values(self):
        assert normalize_range_field((0.0, 1.0, 0.1)) == (0.0, 1.0, 0.1)

    def test_invalid_type(self):
        with pytest.raises(ValueError):
            normalize_range_field(("a",))
        with pytest.raises(ValueError):
            normalize_range_field((1, "b"))
        with pytest.raises(ValueError):
            normalize_range_field((1, 2, 3, 4))
        with pytest.raises(ValueError):
            normalize_range_field([])


class TestRangeFieldToList:
    def test_single_value(self):
        assert range_field_to_list((5,)) == [0, 1, 2, 3, 4]

    def test_two_values(self):
        assert range_field_to_list((2, 8)) == [2, 3, 4, 5, 6, 7]

    def test_three_values(self):
        assert range_field_to_list((1, 10, 2)) == [1, 3, 5, 7, 9]

    def test_float_values(self):
        result = range_field_to_list((0.0, 1.0, 0.3))
        assert len(result) == 4
        assert result[0] == 0.0
        assert result[-1] < 1.0

    def test_invalid_type(self):
        with pytest.raises(ValueError):
            range_field_to_list(("a",))

