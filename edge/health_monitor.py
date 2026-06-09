from config.threshold_loader import load_thresholds
from edge.anomaly_detector import detect_vibration_anomaly


def evaluate_health(data):

    thresholds = load_thresholds()

    alerts = []

    if data["temperature"] >= thresholds["temp_critical"]:
        alerts.append("CRITICAL_TEMPERATURE")
    elif data["temperature"] >= thresholds["temp_warning"]:
        alerts.append("HIGH_TEMPERATURE")

    if data["vibration"] >= thresholds["vibration_critical"]:
        alerts.append("CRITICAL_VIBRATION")
    elif data["vibration"] >= thresholds["vibration_warning"]:
        alerts.append("HIGH_VIBRATION")

    if detect_vibration_anomaly(data["vibration"]):
        alerts.append("VIBRATION_ANOMALY")

    if data["pressure"] <= thresholds["pressure_critical"]:
        alerts.append("CRITICAL_PRESSURE")
    elif data["pressure"] <= thresholds["pressure_warning"]:
        alerts.append("LOW_PRESSURE")

    if (
        any(alert.startswith("CRITICAL") for alert in alerts)
        or "VIBRATION_ANOMALY" in alerts
    ):
        status = "CRITICAL"

    elif alerts:
        status = "WARNING"

    else:
        status = "NORMAL"

    return status, alerts