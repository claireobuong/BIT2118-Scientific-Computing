
from decimal import Decimal

# Simulate a simple banking calculation
transaction_amounts = [0.10, 0.20, 0.30, 0.40, 0.50]

# Calculate the total using floating-point arithmetic
float_total = sum(transaction_amounts)

# Calculate the total using decimal arithmetic
decimal_amounts = [
    Decimal("0.10"),
    Decimal("0.20"),
    Decimal("0.30"),
    Decimal("0.40"),
    Decimal("0.50")
]

decimal_total = sum(decimal_amounts)

print("BANKING TRANSACTION REPORT")
print("Number of transactions:", len(transaction_amounts))
print("Expected total: KSh 1.50")
print("Floating-point total: KSh", format(float_total, ".17f"))
print("Decimal arithmetic total: KSh", decimal_total)
print("Floating-point total equals 1.50:", float_total == 1.50)
print("Decimal total equals 1.50:", decimal_total == Decimal("1.50"))

# Calculate the difference between the two totals
difference = abs(Decimal(str(float_total)) - decimal_total)

print("Difference between totals: KSh", difference)
