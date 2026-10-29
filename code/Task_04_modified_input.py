
import numpy as np

# Modified input values
calculated = 0.1 + 0.3
expected = 0.4

print("TASK 04: MODIFIED FLOATING-POINT INPUT")
print("0.1 + 0.3 =", calculated)
print("Expected value:", expected)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# Modified approximation of square root of 2
true_value = np.sqrt(2)
approx_value = 1.4142

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nMODIFIED NUMERICAL ERROR ANALYSIS")
print("True value of square root of 2:", true_value)
print("Approximate value:", approx_value)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)
print("Relative error percentage:", relative_error * 100, "%")
