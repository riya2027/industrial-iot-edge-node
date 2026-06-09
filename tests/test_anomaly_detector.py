from edge.anomaly_detector import detect_vibration_anomaly


def test_vibration_anomaly():

    detect_vibration_anomaly(2)
    detect_vibration_anomaly(2)
    detect_vibration_anomaly(2)
    detect_vibration_anomaly(2)
    detect_vibration_anomaly(2)

    result = detect_vibration_anomaly(10)

    assert result is True