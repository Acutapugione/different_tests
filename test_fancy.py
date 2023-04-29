# in test_fancy.py
from nose2.tools import params

@params("Sir Bedevere", 1, "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')