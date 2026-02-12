credit_score = float(input("Enter credit score: "))
income = float(input("Enter annual income: $"))

# Classify loan risk based on score and income
if credit_score >= 720 and income >= 60000:
    risk = "Low Risk"
elif credit_score >= 650 and income >= 40000:
    risk = "Medium Risk"
else:
    risk = "High Risk"

# Display result
print(f"\nLoan Risk Category: {risk}")
