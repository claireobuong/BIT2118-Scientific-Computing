import numpy as np
import matplotlib.pyplot as plt

# Fish population in a pond: logistic growth
# dP/dt = r * P * (1 - P/K)
# Assumptions: r = 0.4 per month, carrying capacity K = 1000 fish,
# starting with 50 fish. Compare Euler with three step sizes.
r, K, P0 = 0.4, 1000.0, 50.0
end_time = 12.0

def exact(t):
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

t_plot = np.linspace(0, end_time, 300)
plt.plot(t_plot, exact(t_plot), "k", label="Exact")

for h in (2.0, 1.0, 0.25):
    t = np.arange(0, end_time + h / 2, h)
    P = np.zeros_like(t)
    P[0] = P0
    for i in range(len(t) - 1):
        P[i + 1] = P[i] + h * r * P[i] * (1 - P[i] / K)
    err = abs(P[-1] - exact(t[-1]))
    print(f"h={h:<5} Euler P(12)={P[-1]:8.2f}  exact={exact(12):8.2f}  error={err:.3f}")
    plt.plot(t, P, marker="o", markersize=3, label=f"Euler h={h}")

plt.xlabel("Time (months)")
plt.ylabel("Fish population")
plt.title("Logistic growth: effect of Euler step size")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/Task_17_logistic_growth.png", dpi=150)
plt.show()
