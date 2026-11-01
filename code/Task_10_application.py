import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Break-even point of a small business.
# Assumptions: price = 30 per unit, fixed cost = 1000,
# variable cost = 10 per unit plus a handling cost 5*sqrt(q).
# Profit(q) = 30q - (1000 + 10q + 5*sqrt(q)); break-even where Profit = 0.
def profit(q):
    return 30*q - (1000 + 10*q + 5*np.sqrt(q))

sol = root_scalar(profit, bracket=[1, 200], method="bisect", xtol=1e-10)

# Fixed-point form: q = (1000 + 5*sqrt(q)) / 20
def g(q):
    return (1000 + 5*np.sqrt(q)) / 20

q = 10.0
history = [q]
for _ in range(100):
    q_new = g(q)
    history.append(q_new)
    if abs(q_new - q) < 1e-10:
        break
    q = q_new

print(f"Bisection break-even quantity: {sol.root:.6f} units")
print(f"Bisection iterations: {sol.iterations}")
print(f"Fixed-point break-even quantity: {history[-1]:.6f} units")
print("Fixed-point iterations:", len(history) - 1)
print(f"Profit at break-even: {profit(sol.root):.2e}")

qs = np.linspace(1, 120, 300)
plt.plot(qs, profit(qs))
plt.axhline(0, linewidth=0.8)
plt.axvline(sol.root, linestyle="--")
plt.xlabel("Units sold")
plt.ylabel("Profit")
plt.title("Break-even point")
plt.grid(True)
plt.savefig("docs/images/Task_10_break_even.png", dpi=150)
plt.show()
