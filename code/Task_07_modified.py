
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Real-world application: Heat distribution in three connected rooms.
#
# x1 = temperature rise in room 1 above the surrounding temperature
# x2 = temperature rise in room 2 above the surrounding temperature
# x3 = temperature rise in room 3 above the surrounding temperature
#
# The coefficient matrix represents heat-loss and heat-transfer
# relationships between the three rooms.
#
# The right-hand side represents heat supplied to each room.

A = np.array([
    [4.0, -1.0,  0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0,  3.0]
])

# Heat supplied to the rooms in watts
heat_inputs = [
    np.array([20.0, 12.0, 8.0]),
    np.array([18.0, 14.0, 12.0]),
    np.array([22.0, 10.0, 15.0])
]

# Factorise the coefficient matrix once
lu, piv = lu_factor(A)

# Calculate temperature rises for each heat-input scenario
for i, b in enumerate(heat_inputs, start=1):
    temperatures = lu_solve((lu, piv), b)

    residual = b - A @ temperatures

    print(f"Heat distribution scenario {i}")
    print("Room 1 temperature rise:", round(temperatures[0], 4), "°C")
    print("Room 2 temperature rise:", round(temperatures[1], 4), "°C")
    print("Room 3 temperature rise:", round(temperatures[2], 4), "°C")
    print("Residual norm:", np.linalg.norm(residual))
    print()
