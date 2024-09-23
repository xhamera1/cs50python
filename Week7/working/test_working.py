from working import convert
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat:cat AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("5:cat AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 1:cat PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to cat:30 PM")
    with pytest.raises(ValueError):
        convert("5:40 DM to 1:cat PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 1:cat KM")
    with pytest.raises(ValueError):
        convert("time: 5:40 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("5:60 AM to 4:10 PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 1:67 PM")
    with pytest.raises(ValueError):
        convert("0:40 AM to 1:30 PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 0:30 PM")
    assert convert("5:40 AM to 1:10 PM") == "05:40 to 13:10"
    assert convert("12:40 AM to 11:10 PM") == "00:40 to 23:10"
from working import convert
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat:cat AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("5:cat AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 1:cat PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to cat:30 PM")
    with pytest.raises(ValueError):
        convert("5:40 DM to 1:cat PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 1:cat KM")
    with pytest.raises(ValueError):
        convert("time: 5:40 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("5:60 AM to 4:10 PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 1:67 PM")
    with pytest.raises(ValueError):
        convert("0:40 AM to 1:30 PM")
    with pytest.raises(ValueError):
        convert("5:40 AM to 0:30 PM")
    assert convert("5:40 AM to 1:10 PM") == "05:40 to 13:10"
    assert convert("12:40 AM to 11:10 PM") == "00:40 to 23:10"
