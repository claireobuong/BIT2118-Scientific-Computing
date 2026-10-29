# Task 04: Floating-Point Arithmetic and Numerical Errors

## 1. Inputs and Mathematical Operations

**Input:** The original program adds `0.1` and `0.2` and compares the result with `0.3`. It also calculates the square root of 2 and compares its true value with the approximation `1.414`.

**Operations:** The program performs addition and checks the result using exact equality and `np.isclose()`. It also calculates the absolute error, relative error, and relative error percentage.

Absolute error is the difference between the true value and the approximate value, expressed as a positive number. Relative error is calculated by dividing the absolute error by the absolute value of the true value.

## 2. Parameter Change and Results

**Parameter changed:** In a separate copy of the original program, the addition was changed from `0.1 + 0.2` to `0.1 + 0.3`. The approximation of the square root of 2 was also changed from `1.414` to `1.4142`.

**Original result:** The addition produced `0.30000000000000004` instead of exactly `0.3`. The exact comparison returned `False`, while `np.isclose()` returned `True`. The absolute error was approximately `0.00021356`, and the relative error percentage was approximately `0.0151%`.

**Result after the change:** The addition produced `0.4`, and both comparisons returned `True`. The absolute error for the square-root approximation decreased to approximately `0.00001356`, while the relative error percentage decreased to approximately `0.000959%`.

**Explanation:** Changing the square-root approximation to `1.4142` made it closer to the true value, so both errors became smaller. The modified addition also matched the expected value in this example. However, this does not mean that floating-point calculations always give exact results. Small differences can still occur depending on the numbers being used.

## 3. Explanation of the Output

The program displays the addition result, the expected value, and the results of the two comparison methods. It also shows the true and approximate values of the square root of 2 and the errors between them.

The results show that some decimal numbers cannot be represented exactly using the binary format computers use to store floating-point numbers. This explains why `0.1 + 0.2` can produce a result that is slightly different from `0.3`. Using `np.isclose()` helps check whether two values are close enough to be considered equal for a particular calculation.

## 4. Related Real-World Case: Banking Transaction Calculations

**Assumptions**

The modified program represents a simple banking calculation involving five transactions. The expected total is KSh 1.50. It compares the result obtained using floating-point arithmetic with the result obtained using Python's `Decimal` class. The example uses fixed transaction amounts and does not represent a complete banking system.

**Input Data**

The program uses five transaction amounts: KSh 0.10, KSh 0.20, KSh 0.30, KSh 0.40, and KSh 0.50. It adds the amounts using both floating-point and decimal arithmetic. It then compares the totals with KSh 1.50 and calculates the difference between the two results.

**Output**

- Number of transactions: 5
- Expected total: KSh 1.50
- Floating-point total: KSh 1.50000000000000000
- Decimal arithmetic total: KSh 1.50
- Floating-point total equals 1.50: True
- Decimal total equals 1.50: True
- Difference between totals: KSh 0.00

**Interpretation**

Both methods gave a total of KSh 1.50, with no difference between the results in this example. This shows that floating-point arithmetic can give the expected answer in some calculations, even though small errors may occur in others.

The `Decimal` class is useful for handling money because it allows decimal amounts to be represented accurately when created from strings such as `"0.10"` and `"0.20"`. In banking, this can help avoid rounding problems when handling many transactions. The example shows why choosing the right numerical method matters when working with money.