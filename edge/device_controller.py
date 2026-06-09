from sensors.temperature import read_temperature
from sensors.vibration import read_vibration
from sensors.pressure import read_pressure
from sensors.humidity import read_humidity
from sensors.calibration import (
    calibrate_temperature,
    calibrate_vibration,
    calibrate_pressure,
    calibrate_humidity
)


def collect_sensor_data():

    temperature = calibrate_temperature(read_temperature())
    vibration = calibrate_vibration(read_vibration())
    pressure = calibrate_pressure(read_pressure())
    humidity = calibrate_humidity(read_humidity())

    return {
        "temperature": temperature,
        "vibration": vibration,
        "pressure": pressure,
        "humidity": humidity
    }