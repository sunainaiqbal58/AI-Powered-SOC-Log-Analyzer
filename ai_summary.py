import os
from dotenv import load_dotenv
from openai import OpenAI

# Import SOC statistics
from log_statistics import (
    failed_logins,
    successful_logins,
    top_ip,
    top_ip_attempts,
    top_username
)

# Import Risk Information
from risk_engine import (
    risk_score,
    level
)

# Load .env file
load_dotenv()

# Read API Key
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# Create OpenRouter Client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def generate_ai_report():

    messages = [

        {
            "role": "system",
            "content": """
You are an experienced Security Operations Center (SOC) Analyst.
Analyze authentication logs and identify possible threats.
Generate a structured incident report.
Do not invent data. Only use provided evidence.

Follow this exact format:

## Incident Summary
Explain what happened based only on the provided data.

## Threat Level
Mention severity and explain why.

## Evidence
List important indicators such as:
- suspicious IP addresses
- failed login attempts
- targeted usernames
- risk score

## Possible Impact
Explain what could happen if the attack succeeds.

## Recommended Actions
Provide practical SOC response steps.

Rules:
- Do not invent information.
- Use only the given security data.
- Use professional cybersecurity terminology.
Generate a concise SOC incident report for security monitoring.
"""


        },

        {
            "role": "user",
            "content": f"""
Security Incident Data

Failed Login Attempts:
{failed_logins}

Successful Logins:
{successful_logins}

Top Attacking IP:
{top_ip}

Failed Attempts From Top IP:
{top_ip_attempts}

Most Targeted Username:
{top_username}

Risk Score:
{risk_score}

Risk Level:
{level}
"""
        }

    ]

    try:

        response = client.chat.completions.create(

            model="openrouter/free",

            messages=messages

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI Error: {e}"


if __name__ == "__main__":

    report = generate_ai_report()

    print("\n==============================")
    print(" AI SOC INCIDENT REPORT ")
    print("==============================\n")

    print(report)