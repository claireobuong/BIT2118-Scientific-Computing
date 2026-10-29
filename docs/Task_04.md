# Task 04: Floating-Point Arithmetic and Numerical Errors

## 1. Introduction

This task demonstrates how computers handle decimal numbers using floating-point arithmetic and how small numerical errors can occur during calculations. It also shows how the `numpy.isclose()` function and Python's `Decimal` class can help when comparing numerical values and working with money.

## 2. Original Program

The original program demonstrates the difference between exact floating-point comparison and tolerance-based comparison. It also calculates the absolute and relative errors when approximating the square root of 2.

### Inputs

- First calculation: 0.1 + 0.2.
- Expected result: 0.3.
- True value: square root of 2.
- Approximate value: 1.414.

### Mathematical operations

The program calculates the sum of two floating-point numbers and compares it with the expected result. It uses `numpy.isclose()` to check whether the values are sufficiently close.

Absolute error is calculated as:

Absolute error = |True value − Approximate value|

Relative error is calculated as:

Relative error = Absolute error / |True value|

The relative error percentage is obtained by multiplying the relative error by 100.

### Results and interpretation

The calculation of 0.1 + 0.2 produced 0.30000000000000004 instead of exactly 0.3. Therefore, the exact comparison returned `False`, while the tolerance-based comparison returned `True`.

The absolute error when approximating the square root of 2 with 1.414 was approximately 0.00021356. The relative error was approximately 0.00015101, equivalent to 0.0151%.

These results show that floating-point numbers may be stored as approximations because computers use finite binary precision.

## 3. Modified-Input Experiment

The inputs were changed from 0.1 + 0.2 to 0.1 + 0.3, and the approximation of the square root of 2 was changed from 1.414 to 1.4142.

### Results and interpretation

The calculation 0.1 + 0.3 produced 0.4, and both the exact and tolerance-based comparisons returned `True`.

The absolute error decreased to approximately 0.00001356, while the relative error decreased to approximately 0.00000959, equivalent to 0.000959%.

The decrease in both errors shows that using a more precise approximation of the square root of 2 produces a result closer to its true value. However, the successful exact comparison for 0.1 + 0.3 does not mean that all floating-point calculations are exact.

## 4. Modified Program: Banking Transaction Calculations

### Real-world problem

Banking systems calculate transaction totals and account balances. Small numerical inaccuracies can cause problems when many calculations are performed. This program compares ordinary floating-point arithmetic with decimal arithmetic for a set of monetary transactions.

### Assumptions and inputs

The program uses five transactions: KSh 0.10, KSh 0.20, KSh 0.30, KSh 0.40, and KSh 0.50. All transactions are assumed to be valid, and the expected total is KSh 1.50.

The program uses Python's `Decimal` class with string inputs to represent the monetary amounts precisely.

### Mathematical operations

The program adds the five transaction amounts using ordinary floating-point arithmetic and decimal arithmetic. It then compares each total with the expected amount and calculates the absolute difference between the two totals.

### Results and interpretation

Both methods produced a total of KSh 1.50 in this particular example. Both comparisons returned `True`, and the difference between the totals was KSh 0.00.

The result shows that floating-point arithmetic can produce the expected answer in some cases. However, the earlier 0.1 + 0.2 calculation demonstrated that certain decimal values cannot be represented exactly in binary floating-point format.

Using `Decimal` for monetary calculations helps avoid these representation errors when decimal amounts are constructed correctly. A production banking system would also need appropriate rounding rules, transaction validation, and other financial controls.

## 5. Conclusion

This task demonstrated floating-point representation, absolute error, relative error, and the use of tolerance-based comparisons. The modified-input experiment showed how a more precise approximation reduces numerical error. The banking example demonstrated why decimal arithmetic is useful for monetary calculations. Overall, choosing an appropriate numerical representation helps improve the reliability of calculations in scientific computing and real-world applications.