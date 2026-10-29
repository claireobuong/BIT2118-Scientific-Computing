
import numpy as np

# Real-world application: Two-loop DC electrical circuit
# Assumptions: ideal resistors and batteries, steady-state currents.
#
# Loop 1: 10*I1 - 4*I2 = 12
# Loop 2: -4*I1 + 12*I2 = 6
#
# I1 and I2 are the mesh currents in amperes.
# The shared resistor has a resistance of 4 ohms.

R = np.array([
    [10.0, -4.0],
    [-4.0, 12.0]
])

V = np.array([12.0, 6.0])

currents = np.linalg.solve(R, V)
residual = V - R @ currents

print("TASK 06: DC CIRCUIT ANALYSIS")
print(f"Loop 1 current I1: {currents[0]:.4f} A")
print(f"Loop 2 current I2: {currents[1]:.4f} A")
print(
    "Current through shared 4-ohm resistor:",
    f"{currents[0] - currents[1]:.4f} A"
)
print("Verification R @ I:", R @ currents)
print("Residual norm:", np.linalg.norm(residual))
