def calibrate_temperature(value, offset=0.5):
    return round(value + offset, 2)


def calibrate_vibration(value, offset=0.1):
    return round(value + offset, 2)


def calibrate_pressure(value, offset=0.2):
    return round(value + offset, 2)


def calibrate_humidity(value, offset=1.0):
    return round(value + offset, 2)