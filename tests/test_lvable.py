from kattis.lvable import solve

def test_lv_but_not_v():
    assert solve(7, "lovable") == 1

def test_one_l():
    assert solve(6, "google") == 1

def test_no_lv():
    assert solve(4, "code") == 2

def test_contains_lv():
    assert solve(5, "lvxyz") == 0