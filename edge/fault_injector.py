import random


def inject_fault(data):

    fault = random.choice(
        [
            "NONE",
            "OVERHEAT",
            "VIBRATION_FAILURE",
            "PRESSURE_DROP"
        ]
    )

    if fault == "OVERHEAT":
        data["temperature"] = 95

    elif fault == "VIBRATION_FAILURE":
        data["vibration"] = 10

    elif fault == "PRESSURE_DROP":
        data["pressure"] = 1

    return data, fault