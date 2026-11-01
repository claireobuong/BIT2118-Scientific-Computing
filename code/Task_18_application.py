import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# SIR epidemic model for a school of 10,000 people.
# dS/dt = -beta*S*I/N,  dI/dt = beta*S*I/N - gamma*I,  dR/dt = gamma*I
# Assumptions: beta = 0.30/day (contact rate), gamma = 0.10/day
# (recovery, about 10 days infectious), 10 initially infected,
# no births, deaths or vaccination.
N = 10000.0
beta, gamma = 0.30, 0.10

def sir(t, y):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

sol = solve_ivp(sir, (0, 160), [N - 10, 10, 0],
                t_eval=np.linspace(0, 160, 321), rtol=1e-8, atol=1e-8)
S, I, R = sol.y

peak = np.argmax(I)
print("Solver success:", sol.success)
print(f"Basic reproduction number R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak infected: {I[peak]:.0f} people on day {sol.t[peak]:.1f}")
print(f"Total ever infected by day 160: {R[-1] + I[-1]:.0f} ({(R[-1]+I[-1])/N:.1%})")
print(f"Population check S+I+R at end: {S[-1]+I[-1]+R[-1]:.2f}")

plt.plot(sol.t, S, label="Susceptible")
plt.plot(sol.t, I, label="Infected")
plt.plot(sol.t, R, label="Recovered")
plt.xlabel("Day")
plt.ylabel("People")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/Task_18_sir_epidemic.png", dpi=150)
plt.show()
