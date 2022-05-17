from unittest.mock import patch

import pytest

from rocksteady.steady_rocking import SteadyRocking, get_top_villain_health


class TestSteadyRocking(object):
    @pytest.mark.parametrize("value", [5, -5, 100])
    @patch("rocksteady.steady_rocking.takeback")
    def test_rockout(self, mock_takeback, value):
        mock_takeback.return_value = 1
        assert SteadyRocking(value).bebop() == value

    def test_roll(self, lunchbox):
        assert lunchbox + 10 == 30

    @pytest.mark.parametrize("large_load", [10, 5], indirect=True)
    def test_roll2(self, large_load):
        assert large_load > 0

    def test_data_key3(self, add_key3):
        assert add_key3["DATA1"]["key3"] == 20

    def test_get_top_villain_health(self, villain_factory):
        villains = [
            villain_factory("Diablo", 300),
            villain_factory("Roadhog", 600),
            villain_factory("Kassadin", 150),
        ]

        assert get_top_villain_health(villains) == villains[1]
