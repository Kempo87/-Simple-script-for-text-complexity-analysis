from M06L03_list_comprehension_2 import compute_average_length 


def test_spaces():
    got = compute_average_length("one two")
    assert got == 3.0

def test_punctuation():
    got = compute_average_length("one. two")
    assert got == 3.0

def test_numbers():
    got = compute_average_length("one two 12345")
    assert got == 3.0

def test_nicknames():
    got = compute_average_length("one two123")
    assert got == 4.5

def test_multiple():
    got = compute_average_length("aaaaaaaaaa")
    assert got == 10.0

def test_nothing():
    got = compute_average_length("")
    assert got == 0.0



