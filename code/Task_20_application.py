import numpy as np
import matplotlib.pyplot as plt

# Project risk: three sequential phases with uncertain durations (days).
# Each is triangular(min, most likely, max).
# Assumptions: phases are independent and run one after another;
# the contract deadline is 40 days.
rng = np.random.default_rng(42)
N = 100_000
deadline = 40.0

design = rng.triangular(8, 10, 14, N)
build = rng.triangular(15, 20, 30, N)
testing = rng.triangular(5, 7, 12, N)
total = design + build + testing

late = total > deadline
print(f"Mean project duration: {total.mean():.2f} days")
print(f"Standard deviation: {total.std():.2f} days")
print(f"95th percentile duration: {np.percentile(total, 95):.2f} days")
print(f"Probability of missing the {deadline:.0f}-day deadline: {late.mean():.4%}")
print(f"Late cases: {late.sum()} out of {N}")

plt.hist(total, bins=60)
plt.axvline(deadline, linestyle="--", color="black", label="Deadline")
plt.xlabel("Total project duration (days)")
plt.ylabel("Number of simulations")
plt.title("Monte Carlo project-duration risk")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/Task_20_project_delay.png", dpi=150)
plt.show()
