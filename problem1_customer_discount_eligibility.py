purchase_amount = float(input("Enter purchase amount: $"))
member_status = input("Are you a member? (yes/no): ").lower()

# Determine discount based on business rules
if member_status == "yes" and purchase_amount >= 100:
    discount_rate = 0.15
elif member_status == "yes" and purchase_amount < 100:
    discount_rate = 0.05
elif member_status == "no" and purchase_amount >= 150:
    discount_rate = 0.10
else:
    discount_rate = 0.0

# Calculate discount and final price
discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

# Display results
print(f"\nDiscount applied: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")
