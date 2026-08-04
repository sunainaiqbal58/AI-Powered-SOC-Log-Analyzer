from parser import parsed_logs
from report_generator import generate_csv_report

csv_file = generate_csv_report(parsed_logs)

print("CSV Report Generated:")
print(csv_file)