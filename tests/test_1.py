import pytest

def test_1_1():
    assert False

@pytest.mark.dependency(depends=['test_1_1'])
def test_1_2():
    pass