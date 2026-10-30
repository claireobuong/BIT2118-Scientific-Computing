import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Coefficient matrix
A = np.array([
    [4.0, -1.0,  0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0,  3.0]
])

# Modified measurement values
measurement_sets = [
    np.array([20.0, 12.0, 8.0]),
    np.array([18.0, 14.0, 12.0]),
    np.array([22.0, 10.0, 15.0])
]

# Factorise the matrix only once
lu, piv = lu_factor(A)

# Solve each modified measurement set
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)

    residual = b - A @ x

    print(f"Modified measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()
    