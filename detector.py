# detector.py

# Import parsed logs from parser
from parser import parsed_logs

# Risk Score Values
BRUTE_FORCE_SCORE = 30
SUCCESS_AFTER_FAILURE_SCORE = 40
SUSPICIOUS_IP_SCORE = 50

risk_score = 0

# Store failed login attempts
failed_attempts = {}


# Analyze every log entry
for log in parsed_logs:

    # Check failed login
    if log["status"] == "Failed":

        ip = log["ip"]

        # Increase failed attempts count
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1



# Display failed attempts count
print("Failed Login Attempts:")
print(failed_attempts)
 
   # Brute Force Detection Threshold
THRESHOLD = 5


print("\nBrute Force Detection:")
print("-" * 40)


for ip, count in failed_attempts.items():

    if count >= THRESHOLD:
        print("ALERT! Possible Brute Force Attack")
        print(f"Source IP: {ip}")
        print(f"Failed Attempts: {count}")
        risk_score += 30

    else:
        print(f"{ip} is normal ({count} failed attempts)")
    

        # Detect successful login after failed attempts

previous_failures = {}


print("\nSuccessful Login After Failures Detection:")
print("-" * 40)


for log in parsed_logs:

    ip = log["ip"]

    # Store failures
    if log["status"] == "Failed":

        previous_failures[ip] = previous_failures.get(ip, 0) + 1


    # Check success after failures
    elif log["status"] == "Success":

        if ip in previous_failures and previous_failures[ip] > 1:

            print("ALERT! Suspicious Successful Login")
            print(f"Source IP: {ip}")
            print(f"Previous Failed Attempts: {previous_failures[ip]}")
            print(f"Username: {log['username']}")
            risk_score += 40

            # Suspicious IP Detection

suspicious_ips = [
    "192.168.1.60",
    "10.0.0.5"
]


print("\nSuspicious IP Detection:")
print("-" * 40)


for log in parsed_logs:

    ip = log["ip"]

    if ip in suspicious_ips:

        print("ALERT! Suspicious IP Detected")
        print(f"Source IP: {ip}")
        print(f"Username: {log['username']}")
        print(f"Status: {log['status']}")
        risk_score += 50
        print("\nTotal Risk Score:", risk_score)