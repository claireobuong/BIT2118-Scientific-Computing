# Task 10: Root Finding Using the Bisection and Fixed-Point Iteration Methods

## 1. Inputs and Mathematical Operations

**Input:** The program uses a heat-balance model to determine the equilibrium temperature of a system. The model assumes that the heat gained is equal to the heat lost. The temperature is evaluated within the range of 20°C to 40°C, with an initial fixed-point estimate of 30°C.

**Operations:** The program uses two numerical methods to find the temperature at which the heat-balance function equals zero. The first method is the **Bisection Method**, implemented using SciPy's `root_scalar()` function. It repeatedly divides an interval into two halves until it finds the root.

The second method is the **Fixed-Point Iteration Method**. It repeatedly substitutes the previous temperature estimate into the function until the difference between two consecutive estimates becomes sufficiently small. NumPy is used for numerical calculations and generating temperature values, while Matplotlib is used to plot the heat-balance function.

## 2. Parameter Change and Results

**Parameter changed:** The results show that the equilibrium temperature changed from 27.525211°C to 32.017227°C. This indicates that an input or condition in the heat-balance model was modified. However, the exact parameter changed cannot be identified from the supplied outputs alone.

**Original result:**
- Bisection equilibrium temperature: 27.525211°C
- Fixed-point equilibrium temperature: 27.525211°C
- Fixed-point iterations: 13

**Result after the change:**
- Bisection equilibrium temperature: 32.017227°C
- Fixed-point equilibrium temperature: 32.017227°C
- Fixed-point iterations: 12

**Explanation:** The equilibrium temperature increased from 27.525211°C to 32.017227°C after the model was modified. Both numerical methods produced the same temperature in each case, showing that they successfully found the equilibrium point. The fixed-point method required 13 iterations in the original program and 12 iterations after the change.

## 3. Explanation of the Output

The Bisection and Fixed-Point methods both produced an equilibrium temperature of 27.525211°C in the original program. This is the temperature at which the heat gained by the system equals the heat lost.

After the modification, both methods produced an equilibrium temperature of 32.017227°C. The agreement between the two methods shows that the calculated results are consistent.

The graph displays the heat-balance function against temperature. The point where the curve crosses the horizontal zero line represents the equilibrium temperature. The vertical dashed line marks the equilibrium temperature obtained using the Bisection Method.

## 4. Related Real-World Case: Determining the Break-Even Point of a Business

**Assumptions:** A business wants to determine the number of units it must sell to cover its total costs. The break-even point occurs when total revenue equals total cost, meaning the business makes neither a profit nor a loss.

**Input Data:** The program uses the business's revenue and cost functions to determine the break-even quantity. It applies the Bisection and Fixed-Point Iteration methods to find the quantity at which profit becomes zero.

**Output:**
- Bisection break-even quantity: 51.799293 units
- Bisection iterations: 41
- Fixed-point break-even quantity: 51.799293 units
- Fixed-point iterations: 8
- Profit at break-even: 1.67e-09

**Interpretation:** The business needs to sell approximately 51.8 units to reach its break-even point. At this quantity, total revenue is almost equal to total cost. The profit of 1.67e-09 is extremely close to zero, confirming that the business has reached the break-even point. Both methods produced the same result, although the Fixed-Point Method required fewer iterations than the Bisection Method.