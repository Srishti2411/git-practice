import time

log_file = "logs/system.log"
alert_file = "alerts/alerts.log"

print("Monitoring logs... Press Ctrl+C to stop.\n")

with open(log_file, "r") as file:

    file.seek(0,2)

    while True:
        line = file.readline()

        if not line:
            time.sleep(1)
            continue

        if "ERROR" in line:
            alert = "ALERT: ERROR detected -> " + line.strip()
            print(alert)

            with open(alert_file, "a") as a:
                a.write(alert + "\n")

        elif "WARNING" in line:
            alert = "Warning detected -> " + line.strip()
            print(alert)

            with open(alert_file, "a") as a:
                a.write(alert + "\n")

        elif "INFO" in line:
            print("Info ->", line.strip())