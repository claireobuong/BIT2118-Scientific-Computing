import numpy as np
from scipy.integrate import simpson

# River gauge: flow rate Q in m^3/s measured every hour for 8 hours.
# Total volume = integral of Q dt. Multiply by 3600 to convert hours to seconds.
# Assumption: flow varies smoothly between readings.
t_hours = np.arange(0, 9, dtype=float)
Q = np.array([2.0, 2.6, 3.5, 4.8, 5.6, 5.0, 4.1, 3.2, 2.5])

t_seconds = t_hours * 3600
vol_trap = np.trapezoid(Q, t_seconds)
vol_simp = simpson(Q, x=t_seconds)

print(f"Volume (trapezoid): {vol_trap:,.0f} m^3")
print(f"Volume (Simpson):   {vol_simp:,.0f} m^3")
print(f"Difference: {abs(vol_trap - vol_simp):,.0f} m^3 "
      f"({abs(vol_trap - vol_simp)/vol_simp:.3%})")
print(f"Average flow over 8 h: {vol_simp/(8*3600):.3f} m^3/s")
