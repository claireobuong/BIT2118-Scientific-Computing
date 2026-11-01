# Task 16: Numerical Integration Using Trapezoidal and Simpson's Rules

## 1. Inputs and Mathematical Operations

**Input:** The original program uses smart-meter readings representing electrical power consumption measured every two hours over a period of 12 hours.

- Time (hours): [0, 2, 4, 6, 8, 10, 12]
- Power (kW): [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]

**Operations:** The program uses numerical integration to estimate the total electrical energy consumed over the 12-hour period.

It applies two numerical integration methods:

- **Trapezoidal Rule:** Estimates the area under the power-time curve by dividing it into trapezoids and calculating their total area.
- **Simpson's Rule:** Estimates the area under the curve using quadratic approximations between the measured points.

The program uses NumPy's `trapezoid()` function and SciPy's `simpson()` function to calculate the energy consumption. It then calculates the difference between the two estimates to compare their results.

## 2. Parameter Change and Results

**Parameter changed:** The power measurements were changed in the modified version to examine how different electricity consumption readings affect the estimated total energy consumption.

**Original result:**

- Energy using the Trapezoidal Rule: 15.700 kWh.
- Energy using Simpson's Rule: 15.800 kWh.
- Difference between estimates: 0.100 kWh.

**Result after the change:**

- Energy using the Trapezoidal Rule: 17.300 kWh.
- Energy using Simpson's Rule: 17.933 kWh.
- Difference between estimates: 0.633 kWh.

**Explanation:** Changing the power measurements increased the estimated energy consumption using both methods. The Trapezoidal Rule increased from 15.700 kWh to 17.300 kWh, while Simpson's Rule increased from 15.800 kWh to 17.933 kWh.

The difference between the two estimates also increased from 0.100 kWh to 0.633 kWh. This shows that the numerical integration methods can produce different results depending on the shape of the data and how the area under the curve is approximated.

## 3. Explanation of the Output

The program displays the estimated total electrical energy consumption using the two numerical integration methods.

The original results show that the Trapezoidal Rule estimates energy consumption at 15.700 kWh, while Simpson's Rule estimates it at 15.800 kWh.

The small difference of 0.100 kWh indicates that both methods produce closely related estimates for the supplied measurements.

The results demonstrate how numerical integration can be used to calculate accumulated quantities such as electrical energy from measurements collected at different time intervals.

## 4. Related Real-World Case: Estimating Water Volume from River Flow Measurements

**Assumptions**

The modified program represents a water-monitoring system that measures the flow rate of a river over an eight-hour period. The objective is to estimate the total volume of water that passes through the river during that period.

It is assumed that the flow rate changes gradually between measurements and that the recorded readings are accurate. The flow rate is measured in cubic metres per second (m³/s), while the total volume is measured in cubic metres (m³).

**Input Data**

The program uses river flow-rate measurements collected at different times during the eight-hour period.

It applies the Trapezoidal Rule and Simpson's Rule to estimate the total water volume passing through the river. It also calculates the difference between the two estimates and the average flow rate over the eight hours.

**Output**

- Total volume using the Trapezoidal Rule: 111,780 m³.
- Total volume using Simpson's Rule: 111,960 m³.
- Difference between the estimates: 180 m³.
- Percentage difference: 0.161%.
- Average flow rate over 8 hours: 3.888 m³/s.

**Interpretation**

The results show that approximately 111,780 m³ to 111,960 m³ of water passed through the river during the eight-hour period.

The difference of 180 m³ represents only 0.161% of the estimated volume, showing that the two numerical integration methods produced very close results for the supplied measurements.

The average flow rate of 3.888 m³/s indicates the average volume of water passing through the river per second during the monitoring period.

This information can help water resource managers monitor river flow, estimate available water volumes and support decisions involving water supply and flood management.

The example demonstrates how numerical integration can be applied to real-world problems involving the accumulation of quantities over time.