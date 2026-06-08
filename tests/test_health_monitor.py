from edge.health_monitor import evaluate_health


def test_critical_temperature():
    data = {
        "temperature": 90,
        "vibration": 2,
        "pressure": 8,
        "humidity": 40
    }

    status, alerts = evaluate_health(data)

    assert status == "CRITICAL"


def test_warning_temperature():
    data = {
        "temperature": 75,
        "vibration": 2,
        "pressure": 8,
        "humidity": 40
    }

    status, alerts = evaluate_health(data)

    assert status == "WARNING"


def test_normal_conditions():
    data = {
        "temperature": 40,
        "vibration": 2,
        "pressure": 8,
        "humidity": 40
    }

    status, alerts = evaluate_health(data)

    assert status == "NORMAL"