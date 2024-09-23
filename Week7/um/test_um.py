from um import count

def test_count():
    assert count("Um") == 1
    assert count("Um?") == 1
    assert count("Um, whats up?") == 1
    assert count("Um, how are you, um, whats, um your name, um") == 4
    assert count("Um, how are you, um, whats, um, here is your umbrella um") == 4


