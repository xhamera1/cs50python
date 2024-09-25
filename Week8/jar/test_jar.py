from jar import Jar
import pytest

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0
    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0

def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar1 = Jar()
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar1.deposit(-3)
    with pytest.raises(ValueError):
        jar1.deposit(15)
    jar1.deposit(5)
    assert jar1.size == 5


def test_withdraw():
    jar1 = Jar()
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar1.withdraw(3)
    jar1.deposit(10)
    assert jar1.size == 10
    with pytest.raises(ValueError):
        jar1.withdraw(15)
    jar1.withdraw(5)
    assert jar1.size == 5
    with pytest.raises(ValueError):
        jar1.withdraw(-3)



