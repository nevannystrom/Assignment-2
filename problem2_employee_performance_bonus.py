salary = float(input("Enter annual salary: $"))
score = float(input("Enter performance score (0-100): "))

# Determine bonus percentage based on performance score
if score >= 90:
    bonus_rate = 0.20
elif score >= 80:
    bonus_rate = 0.10
elif score >= 70:
    bonus_rate = 0.05
else:
    bonus_rate = 0.0

# Calculate bonus amount
bonus_amount = salary * bonus_rate

# Display results
print(f"\nPerformance Bonus: {bonus_rate * 100:.0f}%")
print(f"Bonus Amount: ${bonus_amount:,.2f}")
