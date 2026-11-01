import numpy as np
import matplotlib.pyplot as plt

# Car speed sampled every 0.5 s (m/s). Estimate acceleration (m/s^2).
# Assumption: straight-line motion, speedometer error is small.
t = np.arange(0, 4.01, 0.5)
v = np.array([0.0, 1.9, 3.6, 5.0, 6.1, 6.9, 7.4, 7.7, 7.8])

acc = np.zeros_like(v)
acc[0] = (v[1] - v[0]) / (t[1] - t[0])                 # forward
for i in range(1, len(t) - 1):
    acc[i] = (v[i + 1] - v[i - 1]) / (t[i + 1] - t[i - 1])   # central
acc[-1] = (v[-1] - v[-2]) / (t[-1] - t[-2])            # backward

check = np.gradient(v, t)       # NumPy's built-in version for comparison

for ti, vi, ai, ci in zip(t, v, acc, check):
    print(f"t={ti:.1f}s  v={vi:.1f}  accel={ai:.2f}  np.gradient={ci:.2f}")
print("Largest difference from np.gradient:", np.max(np.abs(acc - check)).round(4))
print(f"Peak acceleration: {acc.max():.2f} m/s^2 at t={t[np.argmax(acc)]:.1f}s")

plt.plot(t, acc, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated acceleration (m/s^2)")
plt.title("Acceleration from speed data")
plt.grid(True)
plt.savefig("docs/images/Task_15_acceleration.png", dpi=150)
plt.show()
