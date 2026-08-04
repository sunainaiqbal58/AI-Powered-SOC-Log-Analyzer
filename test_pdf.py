from report_generator import generate_pdf_report

pdf = generate_pdf_report(
    85,
    "Critical",
    "192.168.1.50",
    15,
    """
Possible SSH brute-force attack detected.

Recommendations:
- Block the IP
- Enable MFA
- Review authentication logs
"""
)

print(pdf)