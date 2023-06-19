import pytest
import cafeteria as c

def test_getMaxAdditionalDinersCount(nr_seats, min_dist, nr_diners, positions, additional):
    assert c.getMaxAdditionalDinersCount(nr_seats, min_dist, nr_diners, positions) == additional

test_getMaxAdditionalDinersCount(10, 1, 2, [2, 6], 3)
test_getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 4], 1)
