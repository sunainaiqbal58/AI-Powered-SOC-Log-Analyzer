from report_generator import generate_txt_report


report = generate_txt_report(
    85,
    "Critical",
    "192.168.1.50",
    15,
    "Possible SSH brute force attack detected. Block IP immediately."
)


print(report)