

import csv
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from parser import parsed_logs
from datetime import datetime


def generate_txt_report(
        risk_score,
        level,
        attacking_ip,
        failed_attempts,
        ai_report
):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/incident_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"


    with open(filename, "w") as file:

        file.write("AI-Powered SOC Incident Report\n")
        file.write("="*40 + "\n\n")

        file.write(f"Incident Time: {datetime.now()}\n")
        file.write(f"Risk Score: {risk_score}\n")
        file.write(f"Severity Level: {level}\n\n")


        file.write("Threat Information\n")
        file.write("------------------\n")
        file.write(f"Attacking IP: {attacking_ip}\n")
        file.write(f"Failed Attempts: {failed_attempts}\n\n")


        file.write("AI Incident Analysis\n")
        file.write("-------------------\n")
        file.write(ai_report)


    return filename

def generate_csv_report(parsed_logs):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/security_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # CSV Header
        writer.writerow([
            "Date",
            "Time",
            "Username",
            "IP Address",
            "Status"
        ])

        # Write each parsed log
        for log in parsed_logs:

            writer.writerow([
                log["date"],
                log["time"],
                log["username"],
                log["ip"],
                log["status"]
            ])

    return filename

def generate_pdf_report(
    risk_score,
    level,
    attacking_ip,
    failed_attempts,
    ai_report
):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/incident_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI-Powered SOC Incident Report</b>", styles["Heading1"]))

    story.append(Paragraph(f"Generated: {datetime.now()}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Risk Score:</b> {risk_score}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Severity:</b> {level}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Attacking IP:</b> {attacking_ip}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Failed Attempts:</b> {failed_attempts}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>AI Incident Analysis</b>", styles["Heading2"]))

    story.append(Paragraph(ai_report, styles["BodyText"]))

    doc.build(story)

    return filename