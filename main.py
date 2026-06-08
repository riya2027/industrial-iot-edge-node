import time

from edge.device_controller import collect_sensor_data
from edge.health_monitor import evaluate_health
from edge.alert_manager import display_alerts
from edge.logger import log_sensor_data
from edge.fault_injector import inject_fault
from edge.device_stats import get_uptime


def main():

    while True:

        data = collect_sensor_data()

        data, fault = inject_fault(data)

        print(f"\nFault Scenario : {fault}")

        status, alerts = evaluate_health(data)

        log_sensor_data(data, status)

        print("\nIndustrial IoT Edge Node")
        print("-" * 30)

        print(f"Uptime: {get_uptime()}")
        
        for key, value in data.items():
            print(f"{key:<15}: {value}")

        display_alerts(status, alerts)

        time.sleep(5)


if __name__ == "__main__":
    main()