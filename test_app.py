from app import suma, resta


def test_suma():
    assert suma(2, 3) == 5
    assert suma(0, 0) == 0


def test_resta():
    assert resta(6, 3) == 3
    assert resta(0, 0) == 0
