# Task 7: LU Decomposition Using SciPy

## 1. Inputs and Mathematical Operations

This task uses LU decomposition to solve systems of linear equations using the SciPy library. The program uses a 3 × 3 coefficient matrix and three measurement vectors.

The coefficient matrix is:

A = [[4, -1, 0], [-1, 4, -1], [0, -1, 3]]

The measurement vectors are:

- [15, 10, 10]
- [16, 11, 9]
- [14, 12, 11]

The program uses the `lu_factor()` function to factorise the coefficient matrix into LU form. It then uses `lu_solve()` to calculate the unknown values for each measurement vector.

The matrix is factorised only once and reused when solving the three systems. The program also calculates the residual norm to check how accurately the solutions satisfy the original equations.

## 2. Parameter Change and Results

For the modified program, I changed the measurement vectors while keeping the coefficient matrix unchanged.

The new measurement vectors are:

- [20, 12, 8]
- [18, 14, 12]
- [22, 10, 15]

The results obtained were:

- First set: [6.4390, 5.7561, 4.5854]
- Second set: [6.1463, 6.5854, 6.1951]
- Third set: [7, 6, 7]

The results changed because the measurement values were increased or adjusted. For example, the third set produced [7, 6, 7], compared to [5, 5, 5] from the original first measurement set.

The coefficient matrix remained the same, so the program reused its LU factorisation instead of repeating the process.

## 3. Explanation of the Output

The original program produced [5, 5, 5] for the first measurement set. The other measurement sets produced different solutions depending on their input values. The direct solution using NumPy also gave [5, 5, 5] for the first set, confirming that both methods produced the same result.

After changing the measurement values, the solutions also changed. This shows how the input values affect the unknown variables.

The residual norms in both programs were zero or extremely close to zero. This means that the calculated solutions satisfy the original systems of equations with very little error.

## 4. Related Real-World Case: Heat Distribution in Three Connected Rooms

LU decomposition can also be applied to a simplified problem involving heat distribution in three connected rooms. In this example, the program calculates how much the temperature rises in each room when different amounts of heat are supplied.

### Assumptions

- The three rooms are connected and can exchange heat.
- The system has reached a steady state, meaning the temperatures are no longer changing.
- The heat-transfer relationships between the rooms remain constant.
- Heat transfer is represented using a simplified linear mathematical model.

### Input Data

The same coefficient matrix used in the original task is applied to represent the heat-loss and heat-transfer relationships between the three rooms.

The unknown values represent the temperature rises in the rooms above the surrounding temperature:

- x1 represents the temperature rise in room 1.
- x2 represents the temperature rise in room 2.
- x3 represents the temperature rise in room 3.

Three heat-input scenarios are used:

- [20, 12, 8] watts
- [18, 14, 12] watts
- [22, 10, 15] watts

The program factorises the coefficient matrix once and uses the same LU decomposition to solve all three scenarios.

### Output

The program produced the following temperature rises:

- **Scenario 1:** Room 1 = 6.439°C, Room 2 = 5.7561°C, Room 3 = 4.5854°C.
- **Scenario 2:** Room 1 = 6.1463°C, Room 2 = 6.5854°C, Room 3 = 6.1951°C.
- **Scenario 3:** Room 1 = 7°C, Room 2 = 6°C, Room 3 = 7°C.

The residual norms were zero or extremely close to zero in all three scenarios.

### Interpretation

The results show that the temperature rise in each room depends on the amount of heat supplied and the heat-transfer relationships between the rooms. When the heat inputs change, the calculated temperature rises also change.

The values represent temperature increases above the surrounding temperature rather than the actual room temperatures. The very small residuals show that the solutions are accurate for the mathematical model used.