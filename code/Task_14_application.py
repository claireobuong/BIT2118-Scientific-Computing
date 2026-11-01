import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Monthly mobile-data demand (GB) on a campus network.
# Model: exponential growth y = a * exp(b * x)
# Assumption: demand keeps growing at a constant percentage rate.
months = np.arange(1, 9, dtype=float)
demand = np.array([120, 135, 150, 172, 190, 215, 242, 270], dtype=float)

def model(x, a, b):
    return a * np.exp(b * x)

params, cov = curve_fit(model, months, demand, p0=[100, 0.1])
a, b = params

pred = model(months, a, b)
rmse = np.sqrt(np.mean((demand - pred)**2))
ss_res = np.sum((demand - pred)**2)
ss_tot = np.sum((demand - demand.mean())**2)
r2 = 1 - ss_res / ss_tot

print(f"Fitted model: y = {a:.2f} * exp({b:.4f} x)")
print(f"Monthly growth rate: {np.exp(b) - 1:.2%}")
print(f"RMSE: {rmse:.2f} GB   R^2: {r2:.4f}")
print(f"Forecast month 10: {model(10, a, b):.1f} GB")
print(f"Forecast month 12: {model(12, a, b):.1f} GB")

x_plot = np.linspace(1, 12, 200)
plt.scatter(months, demand, label="Measured")
plt.plot(x_plot, model(x_plot, a, b), label="Exponential fit")
plt.xlabel("Month")
plt.ylabel("Demand (GB)")
plt.title("Demand growth curve")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/Task_14_growth_curve.png", dpi=150)
plt.show()
