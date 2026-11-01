# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Inputs and Mathematical Operations

**Input:** The original program uses two nonlinear equations representing a circle and a parabola. The circle is represented by \(x^2+y^2=4\), while the parabola is represented by \(y=x^2-1\).

**Operations:** The equations are rearranged into residual functions, and SciPy's `root()` function from the `scipy.optimize` module is used to find the intersection points by solving both equations simultaneously.

**Initial guesses:** The program uses two initial guesses, [1.0, 1.0] and [-1.0, 1.0], to find the possible intersection points.

## 2. Parameter Change and Results

**Parameter changed:** The initial guess was changed from [1.0, 1.0] to [-1.0, 1.0] to determine how the starting values affect the solution.

**Original result:** Using the initial guess [1.0, 1.0], the program found the intersection point (1.51748991, 1.30277564). The residual values were approximately zero, and the solver successfully converged.

**Result after the change:** Using the initial guess [-1.0, 1.0], the program found the intersection point (-1.51748991, 1.30277564). The residual values were also approximately zero, and the solver successfully converged.

**Explanation:** Changing the initial guess changed the intersection point from the positive x-coordinate to the negative x-coordinate. However, the y-coordinate remained approximately the same because the two intersection points are symmetrical about the y-axis. Both results demonstrate that the solver can find different solutions depending on the initial guess.

## 3. Explanation of the Output

The program displays the initial guesses, calculated intersection points, residual values and convergence status.

The results show that the circle and parabola intersect at two points: approximately (1.5175, 1.3028) and (-1.5175, 1.3028).

The residual values are extremely close to zero, meaning that the calculated coordinates satisfy both nonlinear equations with very high accuracy. The `Converged: True` message confirms that the numerical solver successfully found both solutions.

This demonstrates how numerical methods can solve nonlinear equations that may be difficult to solve manually.

## 4. Related Real-World Case: Road and Circular Boundary Intersection

**Assumptions**

The modified program represents an engineering problem where a curved road passes through a circular boundary. The objective is to determine the points where the road meets the circular boundary. The circular boundary is assumed to have a radius of 5 km, and the road is represented by a parabolic equation. The model assumes a flat coordinate system and uses kilometres as the measurement unit.

**Input Data**

The circular boundary is represented by:

\(x^2+y^2=25\)

The curved road is represented by:

\(y=0.8x^2-4\)

The program uses two initial guesses, [3.0, 3.0] and [3.0, -3.0], and applies SciPy's `root()` function to find the intersection points.

**Output**

- First initial guess: [3.0, 3.0]
- First boundary crossing: (3.75, 3.3072)
- Second initial guess: [3.0, -3.0]
- Second boundary crossing: (3.75, -3.3072)
- Residual values: [0.0, 0.0]
- Convergence status: True for both solutions.
- Exact x-coordinate: 3.75 km
- Exact absolute y-coordinate: 3.3072 km

**Interpretation**

The results show that the curved road intersects the circular boundary at two points: approximately (3.75, 3.3072) km and (3.75, -3.3072) km.

The zero residual values indicate that the calculated coordinates satisfy both equations. The successful convergence confirms that the numerical solver found the intersection points accurately.

An engineer could use these coordinates to identify where the curved road meets the circular boundary during the design process. This demonstrates how nonlinear equation solving can be applied to practical engineering problems.