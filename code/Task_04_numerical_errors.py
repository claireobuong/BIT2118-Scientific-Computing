
import numpy as np

# Demonstrate floating-point arithmetic
calculated = 0.1 + 0.2
expected = 0.3

print("TASK 04: FLOATING-POINT ARITHMETIC")
print("0.1 + 0.2 =", calculated)
print("Expected value:", expected)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# Calculate absolute and relative errors
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nNUMERICAL ERROR ANALYSIS")
print("True value of square root of 2:", true_value)
print("Approximate value:", approx_value)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)
print("Relative error percentage:", relative_error * 100, "%")
