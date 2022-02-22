# tests/test_lib.py
from mlproject.distance import haversine

def test_haversine():
    assert type(haversine(48.865070, 2.380009,49.747175, 11.709730 )) == float
