import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "Hi", "Test Failed, Condition not matched!"


def test_secondCreditCard(setup):
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"

