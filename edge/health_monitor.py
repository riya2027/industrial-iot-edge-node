from config.settings import (
    TEMP_WARNING,
    TEMP_CRITICAL,
    VIBRATION_WARNING,
    VIBRATION_CRITICAL,
    PRESSURE_WARNING,
    PRESSURE_CRITICAL
)


def evaluate_health(data):

    alerts = []

    if data["temperature"] >= TEMP_CRITICAL:
        alerts.append("CRITICAL_TEMPERATURE")
    elif data["temperature"] >= TEMP_WARNING:
        alerts.append("HIGH_TEMPERATURE")

    if data["vibration"] >= VIBRATION_CRITICAL:
        alerts.append("CRITICAL_VIBRATION")
    elif data["vibration"] >= VIBRATION_WARNING:
        alerts.append("HIGH_VIBRATION")

    if data["pressure"] <= PRESSURE_CRITICAL:
        alerts.append("CRITICAL_PRESSURE")
    elif data["pressure"] <= PRESSURE_WARNING:
        alerts.append("LOW_PRESSURE")

    if any(alert.startswith("CRITICAL") for alert in alerts):
        status = "CRITICAL"
    elif alerts:
        status = "WARNING"
    else:
        status = "NORMAL"

    return status, alerts