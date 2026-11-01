import numpy as np
from scipy.optimize import minimize

# A farmer mixes two fertilizers to meet nutrient needs at least cost.
# x = kg of Fertilizer 1 (cost 30/kg, 20% N, 10% P)
# y = kg of Fertilizer 2 (cost 40/kg, 10% N, 30% P)
# Need at least 8 kg of nitrogen (N) and 6 kg of phosphorus (P).
# Assumptions: nutrient percentages are exact, prices are fixed.
def cost(z):
    x, y = z
    return 30*x + 40*y

constraints = [
    {"type": "ineq", "fun": lambda z: 0.20*z[0] + 0.10*z[1] - 8},   # nitrogen
    {"type": "ineq", "fun": lambda z: 0.10*z[0] + 0.30*z[1] - 6},   # phosphorus
]
bounds = [(0, None), (0, None)]

sol = minimize(cost, x0=[50, 20], method="SLSQP",
               bounds=bounds, constraints=constraints)
x, y = sol.x

print("Optimization success:", sol.success)
print(f"Fertilizer 1: {x:.3f} kg")
print(f"Fertilizer 2: {y:.3f} kg")
print(f"Nitrogen supplied:   {0.20*x + 0.10*y:.3f} kg (need 8)")
print(f"Phosphorus supplied: {0.10*x + 0.30*y:.3f} kg (need 6)")
print(f"Minimum cost: {sol.fun:.2f}")

# Compare with corner points checked by hand
print("Cost using only Fertilizer 1 (60 kg):", 30*60)
print("Cost using only Fertilizer 2 (80 kg):", 40*80)
