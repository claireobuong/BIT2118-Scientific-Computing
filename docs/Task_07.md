# Task 7: Gaussian Elimination AND LU Decomposition

## 1. Inputs and Mathematical Operations

This task uses a system of linear equations to solve for unknown values using Gaussian elimination and LU decomposition. The program uses a coefficient matrix \(A\) and three different measurement vectors. Since the coefficient matrix remains the same, LU decomposition is used to factorise it once and solve the different systems.

The program uses SciPy's `lu_factor()` function to obtain the LU factors and `lu_solve()` to calculate the solutions for each measurement vector. It also uses NumPy's `np.linalg.solve()` to compare the first solution with the one obtained through LU decomposition.

## 2. Parameter Change and Results

In the modified program, I changed the third diagonal value of the coefficient matrix from `3.0` to `6.0`. I kept the three measurement vectors unchanged to see how changing one value in the matrix would affect the solutions.

In the original program, the solutions were:

- Measurement set 1: `[5.0, 5.0, 5.0]`
- Measurement set 2: `[5.3171, 5.2683, 4.7561]`
- Measurement set 3: `[4.9024, 5.6098, 5.5366]`

After changing the value from `3.0` to `6.0`, the solutions became:

- Measurement set 1: `[4.8256, 4.3023, 2.3837]`
- Measurement set 2: `[5.1512, 4.6047, 2.2674]`
- Measurement set 3: `[4.7093, 4.8372, 2.6395]`

The results show that changing a coefficient in the matrix affects the values obtained, even when the measurement vectors remain the same.

## 3. Explanation of Output

The program successfully solved all three measurement sets. I also compared the first solution with the direct solution obtained using `np.linalg.solve()`. Both methods gave the same results in the original and modified programs.

The residual norms were either zero or extremely close to zero. This means that the calculated solutions satisfy the original equations. The very small differences are due to floating-point precision during calculations.

## 4. Related Real-World Case: Thermal Network of Four Rooms

For the real-world application, I modified the program to represent a thermal network involving four rooms in a building. The coefficient matrix represents the heat-flow relationships between the rooms, while the heat input values change every hour over a period of 24 hours.

### Assumptions

- The heat-flow relationships between the four rooms remain constant.
- The model assumes steady-state conditions for each hourly calculation.
- The heat input values change every hour.
- The model uses generated heat input values for the simulation.

### Inputs and Outputs

The program generates 24 sets of hourly heat input values using NumPy's random number generator with a fixed seed of `7`. It then factorises the coefficient matrix once and uses the same LU factors to calculate the room values for all 24 hours.

The program produced the following results:

- Room values at hour 0: `[9.4878, 11.3591, 10.3914, 7.3271]`
- Room values at hour 23: `[8.4467, 8.4898, 7.5733, 9.7120]`
- Highest calculated value across all rooms and hours: `12.776`
- Maximum residual: `1.4210854715202004e-14`

I also compared the time taken to solve 20,000 systems using the two methods. The results were:

- Using LU decomposition (`lu_solve()`): 0.701 seconds
- Using direct solving (`np.linalg.solve()`): 0.272 seconds

### Interpretation

The results show how LU decomposition can be used in a building thermal model where the heat-flow relationships remain the same but the heat inputs change over time. Instead of factorising the coefficient matrix again for every hour, the program factorises it once and reuses the factors.

The maximum residual was extremely small, showing that the calculated values were accurate. However, the timing test showed that `np.linalg.solve()` was faster than `lu_solve()` in this particular program. This could be because the matrix is small and the repeated function calls affect the execution time.

Overall, this task helped me understand how LU decomposition can be used when solving several systems of linear equations that share the same coefficient matrix.