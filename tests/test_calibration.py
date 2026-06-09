from sensors.calibration import calibrate_temperature


def test_temperature_calibration():

    result = calibrate_temperature(50)

    assert result == 50.5