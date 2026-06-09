from collections import deque

vibration_history = deque(maxlen=5)


def detect_vibration_anomaly(current_vibration):

    if len(vibration_history) < 5:
        vibration_history.append(current_vibration)
        return False

    average = sum(vibration_history) / len(vibration_history)

    vibration_history.append(current_vibration)

    if current_vibration > average * 3:
        return True

    return False