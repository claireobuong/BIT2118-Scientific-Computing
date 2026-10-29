# Task 06: Solving Linear Systems Using NumPy

## 1. Inputs and Mathematical Operations

In this task, NumPy is used to solve two linear equations to find the number of Type A and Type B servers needed to meet certain resource requirements.

The given information is:
- Type A server uses 4 CPU units and 8 GB of memory.
- Type B server uses 2 CPU units and 12 GB of memory.
- The total usage is 20 CPU units and 72 GB of memory.

The program puts the equation coefficients in a matrix called `A` and the total resource values in an array called `b`.

The function `np.linalg.solve()` finds the number of servers of each type. The program also calculates the residual and residual norm to check whether the answers are correct.

## 2. Parameter Change and Results

To see how changing the input values affects the results, I changed the total CPU usage from 20 to 24 units and the memory usage from 72 GB to 80 GB. The other values remained the same.

After running the modified program, I got these results:

- Type A servers: 4
- Type B servers: 4
- Verification output: [24. 80.]
- Residual norm: 0.0

In the original program, the answer was 3 Type A servers and 4 Type B servers. After changing the resource totals, the number of Type A servers increased to 4, while the number of Type B servers remained at 4.

This shows that changing the input values also changes the solution.

## 3. Explanation of the Output

The original program found that 3 Type A servers and 4 Type B servers were needed. When these values were checked, they gave the required totals of 20 CPU units and 72 GB of memory.

In the modified program, the result was 4 Type A servers and 4 Type B servers, which gave the new totals of 24 CPU units and 80 GB of memory.

Both programs produced a residual norm of zero. This means the calculated answers satisfy the equations.

## 4. Related Real-World Case: DC Electrical Circuit Analysis

For the real-world application, I used a two-loop DC electrical circuit. The aim was to find the current flowing through each loop using Kirchhoff's voltage law.

**Assumptions**

- The circuit has two loops.
- The resistors and batteries are treated as ideal components.
- The circuit is operating under steady-state conditions.
- The currents flow in opposite directions through the shared resistor.

**Input Data**

The two circuit equations used in the program are:

- 10I₁ − 4I₂ = 12
- −4I₁ + 12I₂ = 6

The resistance values are stored in matrix `R`, while the voltage values are stored in array `V`.

**Output**

After running the program, I obtained the following results:

- Loop 1 current: 1.6154 A
- Loop 2 current: 1.0385 A
- Current through the shared 4-ohm resistor: 0.5769 A
- Verification output: [12. 6.]
- Residual norm: approximately 0.0000000000000018

**Interpretation**

The results show the current flowing through each of the two loops. The current through the shared 4-ohm resistor is found by subtracting the second loop current from the first.

The verification output gives the same voltage values that were used in the equations. The residual norm is extremely small, rather than exactly zero, because of rounding in computer calculations. This shows that the calculated currents are accurate.

From this application, I was able to see how NumPy can also be used to solve electrical circuit problems involving simultaneous linear equations.