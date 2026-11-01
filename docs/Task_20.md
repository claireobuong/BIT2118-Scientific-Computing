# Task 20: Random Number Generation and Monte Carlo Simulation Using NumPy

## 1. Inputs and Mathematical Operations

**Input:** The original program uses Monte Carlo simulation to estimate the probability of server overload based on randomly generated server demand.

The input values are:

- Server capacity: 1,000 units.
- Mean server demand: 850 units.
- Standard deviation of demand: 120 units.
- Number of simulations: 100,000.
- Random seed: 42.

**Operations:** The program uses NumPy's `random.default_rng()` function to generate random demand values based on a normal distribution.

The `normal()` function generates 100,000 possible demand scenarios using the given mean and standard deviation.

The program then compares each generated demand value with the available server capacity. Any demand value greater than 1,000 units is counted as an overload case.

The overload probability is calculated by dividing the number of overload cases by the total number of simulations.

Matplotlib is used to plot the running overload probability to show how the estimated probability changes as more simulations are performed.

## 2. Parameter Change and Results

**Parameter changed:** The simulation settings were modified in the second version to examine how changes in server demand conditions affect the probability of overload.

**Original result:**

- Estimated overload probability: 10.6160%.
- Number of overload cases: 10,616 out of 100,000.

**Result after the change:**

- Estimated overload probability: 33.5940%.
- Number of overload cases: 33,594 out of 100,000.

**Explanation:**

The estimated overload probability increased from 10.6160% to 33.5940%. This means that the modified simulation produced more cases where server demand exceeded the available capacity.

The increase shows that changes in demand conditions can affect the risk of server overload. The simulation helps an organization estimate this risk before it affects the actual server system.

## 3. Explanation of the Output

The program displays the estimated overload probability and the total number of overload cases found during the simulation.

The original result shows that 10,616 out of 100,000 simulated demand scenarios exceeded the available server capacity. This represents an estimated overload probability of 10.6160%.

The modified result shows 33,594 overload cases, giving a higher estimated probability of 33.5940%.

The random seed of 42 helps produce consistent results when the program is run again with the same settings.

The graph shows how the estimated overload probability changes as the number of simulations increases. As more simulations are performed, the estimate generally becomes more stable.

These results show how Monte Carlo simulation can help organizations estimate server risks and make better decisions about their system capacity.

## 4. Related Real-World Case: Estimating Project Completion Time Using Monte Carlo Simulation

**Assumptions:**

The modified program represents a project manager who wants to estimate how long a project is likely to take and determine the risk of missing a 40-day deadline.

The project duration is estimated using repeated random simulations. The model assumes that the possible project durations can be represented by the probability distributions defined in the program.

**Input Data:**

- Number of simulations: 100,000.
- Project deadline: 40 days.
- Simulated project durations are used to estimate the average completion time, variation in duration and probability of finishing late.

**Output:**

- Mean project duration: 40.33 days.
- Standard deviation: 3.68 days.
- 95th percentile duration: 46.72 days.
- Probability of missing the 40-day deadline: 51.2910%.
- Late cases: 51,291 out of 100,000.

**Interpretation:**

The results show that the average project completion time is 40.33 days, which is slightly longer than the planned deadline of 40 days.

The standard deviation of 3.68 days shows how much the simulated project durations vary around the average.

The 95th percentile of 46.72 days means that approximately 95% of the simulated projects are expected to finish within 46.72 days.

The probability of missing the deadline is 51.2910%, meaning that more than half of the simulated projects took longer than the planned 40 days.

This information can help project managers identify possible delays, prepare for unexpected challenges and allocate enough time and resources to complete projects successfully.