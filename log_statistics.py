# log_statistics.py

# Import parsed logs
from parser import parsed_logs


# Total logs
total_logs = len(parsed_logs)


# Counters
failed_logins = 0
successful_logins = 0


# Count login status
for log in parsed_logs:

    if log["status"] == "Failed":
        failed_logins += 1

    elif log["status"] == "Success":
        successful_logins += 1



# ==========================
# Top Attacking IP
# ==========================

ip_counts = {}

for log in parsed_logs:

    if log["status"] == "Failed":

        ip = log["ip"]

        ip_counts[ip] = ip_counts.get(ip, 0) + 1



# Default values (AI ke liye)
top_ip = "No suspicious IP found"
top_ip_attempts = 0


if ip_counts:

    top_ip = max(ip_counts, key=ip_counts.get)

    top_ip_attempts = ip_counts[top_ip]



# ==========================
# Most Targeted Username
# ==========================

username_counts = {}


for log in parsed_logs:

    if log["status"] == "Failed":

        username = log["username"]

        username_counts[username] = username_counts.get(username, 0) + 1



# Default value
top_username = "No targeted username found"



if username_counts:

    top_username = max(
        username_counts,
        key=username_counts.get
    )



# ==========================
# Login Success Ratio
# ==========================

success_rate = 0
failure_rate = 0


if total_logs > 0:

    success_rate = (successful_logins / total_logs) * 100

    failure_rate = (failed_logins / total_logs) * 100




# ==========================
# Display Statistics
# ==========================

if __name__ == "__main__":

    print("\nLog Statistics")
    print("-" * 40)

    print(f"Total Logs        : {total_logs}")

    print(f"Failed Logins     : {failed_logins}")

    print(f"Successful Logins : {successful_logins}")



    print("\nTop Attacking IP")
    print("-" * 40)

    print(f"IP Address      : {top_ip}")

    print(f"Failed Attempts : {top_ip_attempts}")



    print("\nMost Targeted Username")
    print("-" * 40)

    print(f"Username        : {top_username}")



    print("\nLogin Statistics")
    print("-" * 40)

    print(f"Success Rate : {success_rate:.2f}%")

    print(f"Failure Rate : {failure_rate:.2f}%")