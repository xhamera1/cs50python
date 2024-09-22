from numb3rs import validate


def test_numbers():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("300.300.1.1") == False
    assert validate("0.0.0.0") == True
    assert validate("1.300.300.300") == False

def test_syntax():
    assert validate("cat") == False
    assert validate("1.1.1.1.") == False
    assert validate("cat.dog.elo.test") == False
    assert validate("10.240.30.5") == True
