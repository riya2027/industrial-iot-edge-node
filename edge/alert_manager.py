def display_alerts(status, alerts):

    print("\n========================")
    print(f"STATUS : {status}")
    print("========================")

    if alerts:
        for alert in alerts:
            print(f"ALERT : {alert}")
    else:
        print("No Alerts")