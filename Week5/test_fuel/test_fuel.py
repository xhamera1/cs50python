import pytest
from fuel import convert, gauge

def test_convert():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    assert convert("1/4") == 25
    assert convert("1/1") == 100


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


