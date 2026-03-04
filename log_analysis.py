info_count = 0
warning_count = 0
error_count = 0

with open("system.log", "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

report = f"""
Log Analysis Report
-------------------
INFO: {info_count}
WARNING: {warning_count}
ERROR: {error_count}
"""

print(report)

with open("log_report.txt", "w") as report_file:
    report_file.write(report)