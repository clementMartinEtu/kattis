from kattis.floors import solve

def test_first_floor():
    assert solve(1) == 1

def test_thirteenth_floor():
    assert solve(13) == 14