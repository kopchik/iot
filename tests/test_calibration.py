from ..calibration import interpolate

def test_interpolate():
    cal = {
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
    }
    assert interpolate(cal, 0.5) == 5
    assert interpolate(cal, 1) == 10
    assert interpolate(cal, 1.5) == 15
    assert interpolate(cal, 2) == 20
    assert interpolate(cal, 5.5) == 55

# TODO: test negative slope