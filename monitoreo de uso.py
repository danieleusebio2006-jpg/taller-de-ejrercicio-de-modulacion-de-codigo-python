def monitor_server_usage_basic():
    critical_alerts = 0
    usage = 0
    while usage >= 0:
        usage = int(input("CPU usage (%): "))
        if usage > 90:
            critical_alerts = critical_alerts + 1
            print("Alert: Critical Usage")
    print("Total alerts:", critical_alerts)

monitor_server_usage_basic()