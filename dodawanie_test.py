from dodawanie import dodawanie

def test_dodawanie_liczb_dodatnich():
    assert dodawanie(2, 3) == 5

def test_dodawanie_liczb_ujemnych():
    assert add(-2, -3) == -5

def test_dodawanie_liczb_roznych():
    assert add(2, -3) == -1
