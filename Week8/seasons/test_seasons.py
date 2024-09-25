from seasons import calculate
import pytest

def test_calculate():
     with pytest.raises(TypeError):
         calculate(12-12-2012) == 'Invalid date'
