import csv
import os
from datetime import datetime

from config.settings import LOG_FILE


def log_sensor_data(data, status):

    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "temperature",
                "vibration",
                "pressure",
                "humidity",
                "status"
            ])

        writer.writerow([
            datetime.now(),
            data["temperature"],
            data["vibration"],
            data["pressure"],
            data["humidity"],
            status
        ])