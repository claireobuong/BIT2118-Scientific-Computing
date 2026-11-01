import numpy as np
from scipy.optimize import root

# Two phone towers. Tower 1 at (0, 0) covers radius 5 km;
# tower 2 at (6, 0) covers radius 4 km. Find where the two
# coverage boundaries cross (coordinates in km).
# Assumptions: flat terrain, circular coverage.
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 25,
        (x - 6)**2 + y**2 - 16
    ]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    sol = root(equations, guess)
    print("Initial guess:", guess)
    print("Boundary crossing (km):", sol.x.round(4))
    print("Residuals:", np.round(equations(sol.x), 12))
    print("Converged:", sol.success)
    print()

# Exact check from algebra: x = 3.75, y = +/- sqrt(10.9375)
print("Exact x:", 3.75, " Exact |y|:", round(np.sqrt(10.9375), 4))
