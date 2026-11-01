# Task 19: Numerical Optimization Using SciPy

## 1. Inputs and Mathematical Operations

The program uses Python's SciPy `minimize()` function from the `scipy.optimize` library to find the cheapest way of allocating Type A and Type B servers while meeting a required capacity.

The inputs used in the original program are:

- Type A server costs 12 units and provides a capacity of 100 units.
- Type B server costs 18 units and provides a capacity of 170 units.
- The required total capacity is at least 1,000 units.
- The initial allocation is 5 Type A servers and 3 Type B servers.
- The number of servers allocated cannot be negative.

The program defines a cost function to calculate the total cost of the servers. It also defines a capacity constraint to ensure that the selected servers provide enough capacity.

The `minimize()` function uses the SLSQP method to find the allocation with the lowest cost while satisfying the given constraint.

## 2. Parameter Change and Results

In the modified version, the required total capacity was increased from 1,000 to 1,500 units to see how the change would affect the server allocation and total cost.

**Original output:**

- Optimization success: True
- Type A allocation: 0.000
- Type B allocation: 5.882
- Total capacity: 1,000.00
- Minimum planning cost: 105.88
- Best nearby integer solution: (108, 0, 6, 1020)

**Modified output:**

- Optimization success: True
- Type A allocation: 0.000
- Type B allocation: 8.824
- Total capacity: 1,500.00
- Minimum planning cost: 158.82
- Best nearby integer solution: (162, 0, 9, 1530)

**Explanation:**

When the required capacity increased from 1,000 to 1,500 units, the number of Type B servers also increased from approximately 6 to 9. The minimum planning cost increased from 105.88 to 158.82. This happened because more server capacity was needed to meet the new requirement. Type B servers were selected because they provide more capacity at a lower cost per capacity unit.

## 3. Explanation of the Output

The output shows the allocation of servers that gives the lowest cost while meeting the required capacity.

- **Optimization success:** True means that the optimization process completed successfully.
- **Type A allocation:** Shows the number of Type A servers selected.
- **Type B allocation:** Shows the number of Type B servers selected.
- **Total capacity:** Shows the combined capacity provided by the selected servers.
- **Minimum planning cost:** Shows the lowest cost obtained from the optimization.
- **Best nearby integer solution:** Shows the cheapest whole-number combination of servers that meets the required capacity.

The results show that Type B servers are more economical for this particular problem. The whole-number solution is also useful because servers are normally purchased as complete units rather than fractions.

## 4. Related Real-World Case: Optimizing Fertilizer Costs on a Farm

**Assumptions:**

A farmer wants to buy two types of fertilizers to provide enough nitrogen and phosphorus for a farm. The farmer needs to meet the required nutrient levels while spending as little money as possible. The fertilizers can be mixed in different quantities.

**Input Data:**

- Fertilizer 1 costs 30 per kg.
- Fertilizer 2 costs 40 per kg.
- Required nitrogen: 8 kg.
- Required phosphorus: 6 kg.

**Output:**

- Fertilizer 1 allocation: 36 kg.
- Fertilizer 2 allocation: 8 kg.
- Nitrogen supplied: 8 kg.
- Phosphorus supplied: 6 kg.
- Minimum cost: 1,400.
- Cost using only Fertilizer 1 (60 kg): 1,800.
- Cost using only Fertilizer 2 (80 kg): 3,200.

**Interpretation:**

The results show that using 36 kg of Fertilizer 1 and 8 kg of Fertilizer 2 provides the required amounts of nitrogen and phosphorus at a total cost of 1,400. This is cheaper than using either fertilizer alone. The example shows how numerical optimization can help farmers choose the right combination of resources while reducing costs.