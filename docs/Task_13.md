# Task 13: Interpolation Using Linear and Cubic Spline Methods

## 1. Inputs and Mathematical Operations

**Input:** The program uses hourly temperature measurements collected between 8:00 AM and 2:00 PM.

- Hours: [8, 9, 10, 11, 12, 13, 14]
- Temperatures: [18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0] °C
- Target time: 10:30 AM.

**Operations:** The program uses two interpolation methods from SciPy's `scipy.interpolate` module.

- **Linear interpolation:** Estimates temperatures between two known measurements by assuming a straight-line relationship.
- **Cubic spline interpolation:** Uses cubic polynomial functions to produce a smooth curve through the known measurements.

The program generates temperature estimates at 10-minute intervals between 8:00 AM and 2:00 PM. It also plots the original measurements together with the linear and cubic interpolation curves.

## 2. Parameter Change and Results

**Parameter changed:** The target time was changed from 10:30 AM to another measurement point to compare how the interpolation methods estimate temperatures using different input times and data.

**Original result at 10:30 AM:**
- Linear estimate: 23.25 °C
- Cubic estimate: 23.36 °C

**Result from the changed version:**
- Linear estimate: 23.25 °C
- Cubic estimate: 22.99 °C

**Explanation:** The linear estimates remained the same, while the cubic estimates changed. This shows that the two interpolation methods can produce different estimates depending on the measurement data and the position being estimated. Linear interpolation uses the two surrounding measurements, while cubic spline interpolation considers the overall shape of the data to produce a smooth curve.

## 3. Explanation of the Output

The program displays the estimated temperature at 10:30 AM using both interpolation methods.

The linear method estimates the temperature as 23.25 °C, while the cubic spline method estimates it as 23.36 °C. The small difference occurs because the methods use different mathematical approaches.

The program also generates a graph showing the original hourly temperature measurements and the two interpolation curves. The scatter points represent the actual recorded temperatures, while the lines show the estimated temperatures between the recorded hours.

The graph helps compare the two methods and shows how temperature changes throughout the day.

## 4. Related Real-World Case: Estimating Missing Water Level Measurements

**Assumptions**

The modified program represents a water-monitoring system that records water levels at different times during the day. Some readings may be missing because of temporary sensor failure. The program uses interpolation to estimate the missing readings.

It is assumed that the water level changes gradually between recorded measurements and that the available readings are accurate.

**Input Data**

The program uses recorded water levels at different times of the day. It estimates a missing reading at 9:00 AM using linear interpolation and cubic spline interpolation.

The program also generates a continuous series of estimated water levels at 30-minute intervals.

**Output**

- Missing 9:00 AM reading using linear interpolation: 76.50
- Missing 9:00 AM reading using cubic spline interpolation: 84.19
- The cubic spline method generates the following 30-minute water-level series:

  [35.0, 38.4, 48.0, 60.4, 72.0, 80.1, 84.2, 84.4, 81.0, 74.3, 66.0, 57.9, 52.0]

**Interpretation**

The results show that both interpolation methods can estimate missing water-level measurements using the available readings. However, the methods produce different estimates, with linear interpolation giving 76.50 and cubic spline interpolation giving 84.19.

The 30-minute series provides a more detailed picture of how the water level changes over time. This can help water resource managers monitor water levels even when some sensor readings are missing.

The example demonstrates how interpolation can be used in real-world monitoring systems to estimate missing data and support decision-making.