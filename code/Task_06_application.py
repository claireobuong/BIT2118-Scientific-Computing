import numpy as np

# Two-loop DC circuit, mesh-current analysis (Kirchhoff's voltage law)
# Assumptions: ideal resistors and batteries, steady state
# Loop 1: 10*I1 - 4*I2 = 12   (12 V source, 6 ohm + 4 ohm shared branch)
# Loop 2: -4*I1 + 12*I2 = 6   (6 V source)
R = np.array([
    [10.0, -4.0],
    [-4.0, 12.0]
])
V = np.array([12.0, 6.0])

I = np.linalg.solve(R, V)
residual = V - R @ I

print(f"Loop 1 current I1: {I[0]:.4f} A")
print(f"Loop 2 current I2: {I[1]:.4f} A")
print(f"Current through shared 4-ohm resistor: {I[0]-I[1]:.4f} A")
print("Verification R @ I:", R @ I)
print("Residual norm:", np.linalg.norm(residual))
