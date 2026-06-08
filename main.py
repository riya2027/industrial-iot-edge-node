from edge.device_controller import collect_sensor_data
from edge.health_monitor import evaluate_health
from edge.alert_manager import display_alerts


def main():

    data = collect_sensor_data()

    status, alerts = evaluate_health(data)

    print("\nIndustrial IoT Edge Node")
    print("-" * 30)

    for key, value in data.items():
        print(f"{key:<15}: {value}")

    display_alerts(status, alerts)


if __name__ == "__main__":
    main()