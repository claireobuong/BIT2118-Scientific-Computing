# Task 18: Solving Ordinary Differential Equations Using SciPy

## 1. Inputs and Mathematical Operations

**Input:** The original program models the charging process of a capacitor in an RC electrical circuit.

The input values are:

- Supply voltage (\(V_s\)): 5 V.
- Resistance (\(R\)): 1,000 ohms.
- Capacitance (\(C\)): 0.001 farads.
- Initial capacitor voltage (\(V_0\)): 0 V.
- Simulation period: 0 to 5 seconds.
- Number of evaluation points: 200.

**Operations:** The program uses the `solve_ivp()` function from SciPy's `scipy.integrate` module to solve an ordinary differential equation describing how the capacitor voltage changes over time.

The charging process is represented by:

\[
\frac{dV}{dt}=\frac{V_s-V}{RC}
\]

The program calculates the capacitor voltage at different time points and compares the numerical solution with the exact mathematical solution.

It also calculates the maximum absolute error to measure the accuracy of the numerical solution. Matplotlib is used to plot the numerical and exact charging curves.

## 2. Parameter Change and Results

**Parameter changed:** The circuit parameters were modified in the second version to examine how changes in the electrical circuit affect the capacitor charging voltage.

**Original result:**

- Solver success: True.
- Capacitor voltage after 5 seconds: 4.9663 V.
- Maximum error against the exact solution: 9.282 × 10⁻¹⁰ V.

**Result after the change:**

- Solver success: True.
- Capacitor voltage after 5 seconds: 4.5896 V.
- Maximum error against the exact solution: 6.740 × 10⁻¹⁰ V.

**Explanation:** The modified version produced a lower capacitor voltage after 5 seconds, decreasing from 4.9663 V to 4.5896 V. This indicates that the changed circuit parameters affected the charging behaviour of the capacitor.

Both versions successfully solved the differential equation. The very small errors show that the numerical solutions were extremely close to their exact mathematical solutions.

## 3. Explanation of the Output

The program displays the solver status, capacitor voltage after 5 seconds and the maximum error between the numerical and exact solutions.

The original result shows that the capacitor voltage reaches 4.9663 V, which is close to the supply voltage of 5 V. This indicates that the capacitor is almost fully charged after 5 seconds.

The message `Solver success: True` confirms that SciPy successfully completed the numerical calculation.

The maximum error of 9.282 × 10⁻¹⁰ V is extremely small, showing that the numerical solution is highly accurate.

The graph compares the charging curve produced by `solve_ivp()` with the exact mathematical curve. The two curves should almost overlap because their difference is very small.

This demonstrates how SciPy can solve differential equations to model the behaviour of real electrical systems.

## 4. Related Real-World Case: Modelling the Spread of an Infectious Disease

**Assumptions**

The modified program represents a disease outbreak in a population of 10,000 people. The objective is to estimate how the number of susceptible, infected and recovered people changes over 160 days.

The model assumes that the population remains constant, there are no births or deaths during the simulation, and individuals who recover become immune. The infection and recovery rates are assumed to remain constant throughout the simulation.

**Input Data**

The program uses the SIR (Susceptible-Infected-Recovered) mathematical model, which divides the population into three groups:

- Susceptible (S): People who can become infected.
- Infected (I): People who currently have the disease.
- Recovered (R): People who have recovered and are assumed to be immune.

The model uses the following parameters:

- Total population: 10,000 people.
- Infection rate (\(\beta\)): 0.3.
- Recovery rate (\(\gamma\)): 0.1.
- Simulation period: 160 days.

SciPy's `solve_ivp()` function is used to solve the differential equations and estimate how the three population groups change over time.

**Output**

- Solver success: True.
- Basic reproduction number (\(R_0\)): 3.0.
- Peak infected population: 3,008 people on day 38.5.
- Total people infected by day 160: 9,405 (94.1%).
- Population check at the end: 10,000 people.

**Interpretation**

The results show that the disease spreads rapidly because the basic reproduction number is 3.0. This means that, under the model's initial conditions, one infected person can infect an average of three other people in a fully susceptible population.

The number of infected people reaches its highest point at approximately day 38.5, with 3,008 people infected. By day 160, approximately 9,405 people have been infected.

The final population check of 10,000 confirms that the total population remains constant throughout the simulation.

This information can help public health officials understand the possible spread of an infectious disease, identify when infections may reach their peak and plan healthcare resources accordingly.