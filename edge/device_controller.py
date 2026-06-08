from sensors.temperature import read_temperature
from sensors.vibration import read_vibration
from sensors.pressure import read_pressure
from sensors.humidity import read_humidity


def collect_sensor_data():
    return {
        "temperature": read_temperature(),
        "vibration": read_vibration(),
        "pressure": read_pressure(),
        "humidity": read_humidity()
    }