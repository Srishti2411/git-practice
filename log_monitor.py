error_count = 0

with open("system.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
            error_count += 1

print("\nTotal errors:", error_count)