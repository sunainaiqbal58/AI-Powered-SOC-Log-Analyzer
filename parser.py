# parser.py

# Import regular expressions module
import re

# Path of the log file
LOG_FILE = "logs/auth.log"


# Open the log file in read mode
with open(LOG_FILE, "r") as file:
    logs = file.readlines()


# Print total number of log entries
print(f"Total Log Entries: {len(logs)}")


# Store all parsed logs
parsed_logs = []


# Process each log entry
for log in logs:

    # Extract Date and Time
    match = re.search(
        r"([A-Z][a-z]{2}\s+\d{1,2})\s+(\d{2}:\d{2}:\d{2})",
        log
    )


    # Continue only if date/time found
    if match:

        date = match.group(1)
        time = match.group(2)


        # Extract Login Status
        if "Failed password" in log:
            status = "Failed"

        elif "Accepted password" in log:
            status = "Success"

        else:
            status = "Unknown"



        # Extract Username
        user_match = re.search(r"for\s+(\w+)", log)

        if user_match:
            username = user_match.group(1)

        else:
            username = "Unknown"



        # Extract IP Address
        ip_match = re.search(
            r"from\s+(\d+\.\d+\.\d+\.\d+)",
            log
        )

        if ip_match:
            ip = ip_match.group(1)

        else:
            ip = "Unknown"



        # Create structured log entry
        log_entry = {
            "date": date,
            "time": time,
            "username": username,
            "ip": ip,
            "status": status
        }


        # Add entry into list
        parsed_logs.append(log_entry)



# Display parsed logs
print("\nParsed Logs:")
print("-" * 40)

for entry in parsed_logs:
    print(entry)