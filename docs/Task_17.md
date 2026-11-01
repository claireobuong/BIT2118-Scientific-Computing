# Task 17: Solving Ordinary Differential Equations Using Euler's Method

## 1. Inputs and Mathematical Operations

**Input:** The original program models the cooling of a hot object using Newton's Law of Cooling.

The input values are:

- Ambient temperature: 25°C.
- Initial temperature: 90°C.
- Cooling constant (\(k\)): 0.12.
- Step size (\(h\)): 1 minute.
- Total cooling time: 30 minutes.

**Operations:** The program uses Euler's method to estimate the temperature of the object over time.

The cooling process is represented by the differential equation:

\[
\frac{dT}{dt}=-k(T-T_{\text{ambient}})
\]

Euler's method calculates the next temperature using the current temperature, the cooling rate and the time step.

The program also calculates the exact temperature using the analytical solution of Newton's Law of Cooling. It then compares the Euler estimate with the exact solution to determine the numerical error.

NumPy is used for numerical calculations, while Matplotlib is used to plot the estimated and exact temperatures.

## 2. Parameter Change and Results

**Parameter changed:** The cooling model was modified in the second version to examine how changing an input parameter affects the estimated temperature and numerical error.

**Original result:**

- Euler temperature after 30 minutes: 26.40°C.
- Exact temperature after 30 minutes: 26.78°C.
- Final absolute error: 0.3720°C.

**Result after the change:**

- Euler temperature after 30 minutes: 25.27°C.
- Exact temperature after 30 minutes: 26.78°C.
- Final absolute error: 1.5098°C.

**Explanation:** The modified version produced a lower estimated temperature than the original version. The absolute error increased from 0.3720°C to 1.5098°C, meaning that the modified Euler estimate was further away from the exact solution.

This demonstrates that changes to the inputs or parameters of a differential equation can affect the numerical results and the accuracy of Euler's method.

## 3. Explanation of the Output

The program displays the estimated temperature using Euler's method, the exact temperature after 30 minutes and the absolute error between the two results.

The original results show that Euler's method estimates the final temperature as 26.40°C, compared with the exact temperature of 26.78°C.

The small difference of 0.3720°C indicates that Euler's method provides a reasonably close approximation for the selected time step.

The graph compares the temperature estimated using Euler's method with the exact cooling curve. It shows how the temperature gradually decreases towards the surrounding temperature of 25°C.

This demonstrates how numerical methods can be used to approximate the solutions of differential equations when studying changing quantities over time.

## 4. Related Real-World Case: Modelling Population Growth

**Assumptions**

The modified program represents a population monitoring system that estimates how a population changes over time. The population is assumed to follow a continuous growth model, and Euler's method is used to approximate its value at different time intervals.

The model uses a fixed growth pattern over the forecasting period. The exact mathematical solution is also calculated to compare the accuracy of Euler's method.

**Input Data**

The program uses a population growth differential equation and estimates the population after 12 time units.

Three different step sizes are tested:

- 2.0 time units.
- 1.0 time unit.
- 0.25 time units.

The program compares the Euler estimates with the exact population value to determine how the step size affects accuracy.

**Output**

- With a step size of 2.0:
  - Euler estimate, P(12): 792.63.
  - Exact value: 864.78.
  - Error: 72.146.

- With a step size of 1.0:
  - Euler estimate, P(12): 837.86.
  - Exact value: 864.78.
  - Error: 26.918.

- With a step size of 0.25:
  - Euler estimate, P(12): 859.21.
  - Exact value: 864.78.
  - Error: 5.572.

**Interpretation**

The results show that the accuracy of Euler's method improves as the step size decreases.

When the step size is 2.0, the error is 72.146, while reducing the step size to 0.25 decreases the error to 5.572.

The estimate of 859.21 obtained using the smallest step size is much closer to the exact value of 864.78.

This demonstrates that using smaller time steps can improve the accuracy of Euler's method. The technique can help population planners estimate future population changes and support decisions involving housing, healthcare and other public services.