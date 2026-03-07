import time

log_file = "logs/system.log"

print("Monitoring logs... Press Ctrl+C to stop.\n")

with open(log_file, "r") as file:
    
    # Move to end of file
    file.seek(0,2)

    while True:
        line = file.readline()

        if not line:
            time.sleep(1)
            continue

        if "ERROR" in line:
            print("ALERT: ERROR detected ->", line.strip())

        elif "WARNING" in line:
            print("Warning detected ->", line.strip())

        elif "INFO" in line:
            print("Info ->", line.strip())