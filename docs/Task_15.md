# Task 15: Numerical Differentiation Using Finite Difference Methods

## 1. Inputs and Mathematical Operations

**Input:** The original program uses GPS measurements containing time values and the corresponding positions of a moving object.

- Time: [0, 1, 2, 3, 4, 5, 6] seconds.
- Position: [0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0] metres.

**Operations:** The program uses numerical differentiation to estimate the speed of the moving object from its position measurements.

It applies three finite difference methods:

- **Forward difference:** Used at the first measurement to estimate speed.
- **Central difference:** Used at the interior measurements to estimate speed using the positions before and after each point.
- **Backward difference:** Used at the last measurement to estimate speed.

The program also uses NumPy to store and process the measurements and Matplotlib to plot the estimated speed against time.

## 2. Parameter Change and Results

**Parameter changed:** The position measurements were modified in the second version to examine how changes in GPS data affect the estimated speed.

**Original result:**

- At 0 seconds: 4.80 m/s.
- At 1 second: 5.10 m/s.
- At 2 seconds: 5.65 m/s.
- At 3 seconds: 6.25 m/s.
- At 4 seconds: 6.95 m/s.
- At 5 seconds: 7.65 m/s.
- At 6 seconds: 8.00 m/s.

**Result after the change:**

- At 0 seconds: 4.80 m/s.
- At 1 second: 5.10 m/s.
- At 2 seconds: 6.85 m/s.
- At 3 seconds: 6.25 m/s.
- At 4 seconds: 5.75 m/s.
- At 5 seconds: 7.65 m/s.
- At 6 seconds: 8.00 m/s.

**Explanation:** Changing the position measurements affected the estimated speeds at some time intervals. For example, the estimated speed at 2 seconds increased from 5.65 m/s to 6.85 m/s, while the speed at 4 seconds decreased from 6.95 m/s to 5.75 m/s.

This demonstrates that numerical differentiation depends on the accuracy of the position measurements. Changes in GPS readings can affect the calculated speed, even when the time intervals remain unchanged.

## 3. Explanation of the Output

The program displays the time, recorded position and estimated speed at each measurement point.

The results show that the object's estimated speed generally increases from 4.80 m/s at the beginning to 8.00 m/s at the final measurement. This indicates that the object is generally moving faster as time progresses.

The graph displays the estimated speed against time. The plotted points represent the calculated speeds at each measurement, while the connecting line shows how the estimated speed changes throughout the period.

The results demonstrate how finite difference methods can be used to estimate the rate of change of position when an exact mathematical function is not available.

## 4. Related Real-World Case: Estimating Vehicle Acceleration from Speed Measurements

**Assumptions**

The modified program represents a vehicle monitoring system that records a vehicle's speed at regular half-second intervals. Numerical differentiation is used to estimate the vehicle's acceleration.

It is assumed that the speed measurements are accurate and that the vehicle moves along a straight road. Acceleration is estimated from the changes in speed over time.

**Input Data**

The program uses the following speed measurements:

- Time intervals: 0.0 to 4.0 seconds, at 0.5-second intervals.
- Speed measurements: [0.0, 1.9, 3.6, 5.0, 6.1, 6.9, 7.4, 7.7, 7.8] m/s.

The program calculates acceleration using finite differences and compares the results with NumPy's `gradient()` function.

**Output**

- At 0.0 seconds: acceleration = 3.80 m/s².
- At 0.5 seconds: acceleration = 3.60 m/s².
- At 1.0 seconds: acceleration = 3.10 m/s².
- At 1.5 seconds: acceleration = 2.50 m/s².
- At 2.0 seconds: acceleration = 1.90 m/s².
- At 2.5 seconds: acceleration = 1.30 m/s².
- At 3.0 seconds: acceleration = 0.80 m/s².
- At 3.5 seconds: acceleration = 0.40 m/s².
- At 4.0 seconds: acceleration = 0.20 m/s².
- Largest difference from NumPy's `gradient()`: 0.0.
- Peak acceleration: 3.80 m/s² at 0.0 seconds.

**Interpretation**

The results show that the vehicle's acceleration is highest at the beginning, at 3.80 m/s², and gradually decreases to 0.20 m/s² at the end of the measurement period.

This means that the vehicle is still increasing its speed, but the rate at which its speed increases is becoming smaller.

The largest difference of 0.0 between the calculated acceleration and NumPy's `gradient()` indicates that both methods produced matching results for the supplied data.

This demonstrates how numerical differentiation can be used in vehicle monitoring systems to estimate acceleration from recorded speed measurements. Such information can help analyse vehicle movement and performance.