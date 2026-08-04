# risk_engine.py

from detector import risk_score


def calculate_risk(score):

    if score >= 80:
        return "Critical"

    elif score >= 50:
        return "High"

    elif score >= 20:
        return "Medium"

    else:
        return "Low"


level = calculate_risk(risk_score)

print("\nRisk Assessment")
print("-" * 40)
print(f"Total Risk Score : {risk_score}")
print(f"Risk Level       : {level}")

if level == "Critical":
    print("Recommendation   : Immediate investigation required!")

elif level == "High":
    print("Recommendation   : Investigate as soon as possible.")

elif level == "Medium":
    print("Recommendation   : Monitor the activity.")

else:
    print("Recommendation   : No immediate action required.")