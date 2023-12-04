import pytest
from my_summ_module import summ_it

def test_1():
    assert summ_it(4, 9) == 13, 'Wrong summ result'

def test_2():
    assert summ_it(7, 8) == 13, 'Wrong summ result'
