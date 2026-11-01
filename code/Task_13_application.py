import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Air-quality sensor (PM2.5, micrograms per m^3). The 09:00 reading is
# missing because the sensor lost power. Estimate it, and also fill the
# series every 30 minutes.
# Assumption: pollution changes smoothly between readings.
hours = np.array([6, 7, 8, 10, 11, 12], dtype=float)
pm25 = np.array([35.0, 48.0, 72.0, 81.0, 66.0, 52.0])

linear = interp1d(hours, pm25, kind="linear")
cubic = CubicSpline(hours, pm25)

print(f"Missing 09:00 reading, linear: {float(linear(9.0)):.2f}")
print(f"Missing 09:00 reading, cubic:  {float(cubic(9.0)):.2f}")

times = np.arange(6, 12.01, 0.5)
print("30-min cubic series:", np.round(cubic(times), 1))

plt.scatter(hours, pm25, label="Recorded")
plt.plot(times, linear(times), label="Linear")
plt.plot(times, cubic(times), label="Cubic spline")
plt.scatter([9.0], [float(cubic(9.0))], marker="x", s=80, label="Estimated 09:00")
plt.xlabel("Hour of day")
plt.ylabel("PM2.5")
plt.title("Filling a missing sensor reading")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/Task_13_missing_reading.png", dpi=150)
plt.show()
