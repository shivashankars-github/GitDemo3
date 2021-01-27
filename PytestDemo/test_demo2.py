import pytest

@pytest.mark.skip
def test_firstprogram():
    msg = "hello"
    assert msg == 'hi', "test failed because string doesn't matched"




def test_secondprogram():
    a = 10
    b = 6
    assert a-4 == b , "assert matched"


def test_getbrowser(crossbrowser):
    print(crossbrowser[1])

