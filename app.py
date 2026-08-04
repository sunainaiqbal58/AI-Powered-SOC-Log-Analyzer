from flask import Flask, render_template, send_from_directory, send_file
from report_generator import (
    generate_txt_report,
    generate_csv_report,
    generate_pdf_report
)
import importlib
from parser import parsed_logs


# Import Log Statistics
from log_statistics import (
    total_logs,
    failed_logins,
    successful_logins,
    top_ip,
    top_ip_attempts,
    top_username,
)

# Import Risk Information
from risk_engine import (
    risk_score,
    level,
)

# Import AI Report
from ai_summary import generate_ai_report


app = Flask(__name__)


# Function to regenerate charts
def regenerate_charts():

    import charts
    import login_ratio_chart
    import top_attacking_ip_chart
    import attack_timeline_chart

    importlib.reload(charts)
    importlib.reload(login_ratio_chart)
    importlib.reload(top_attacking_ip_chart)
    importlib.reload(attack_timeline_chart)



# Route for Dashboard
@app.route("/")
def dashboard():

    # Generate new charts from latest data
    regenerate_charts()

    # Generate AI Incident Report
    ai_report = generate_ai_report()
    print(ai_report)

    return render_template(

        "index.html",

        total_logs=total_logs,

        failed_logins=failed_logins,

        successful_logins=successful_logins,

        top_ip=top_ip,

        top_ip_attempts=top_ip_attempts,

        top_username=top_username,

        risk_score=risk_score,

        risk_level=level,

        ai_report=ai_report

    )


# Route for Chart Images
@app.route("/reports_images/<path:filename>")
def reports_images(filename):

    return send_from_directory("reports_images", filename)

@app.route("/download/txt")
def download_txt():
    

    ai_report = generate_ai_report()

    txt_file = generate_txt_report(
        risk_score,
        level,
        top_ip,
        top_ip_attempts,
        ai_report
    )

    return send_file(txt_file, as_attachment=True)

@app.route("/download/pdf")
def download_pdf():

    ai_report = generate_ai_report()

    pdf_file = generate_pdf_report(
        risk_score,
        level,
        top_ip,
        top_ip_attempts,
        ai_report
    )

    return send_file(pdf_file, as_attachment=True)

@app.route("/download/csv")
def download_csv():

    csv_file = generate_csv_report(parsed_logs)

    return send_file(csv_file, as_attachment=True)


# Run Flask
if __name__ == "__main__":

    app.run(debug=True)