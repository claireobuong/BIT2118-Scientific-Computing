# Task 11: Root Finding Using Newton-Raphson and Secant Methods

## 1. Inputs and Mathematical Operations

The program uses Python's SciPy `root_scalar` function to calculate the Internal Rate of Return (IRR) of an investment using the Newton-Raphson and Secant methods.

The initial investment is Ksh 10,000, followed by four annual cash inflows of Ksh 3,000, Ksh 3,500, Ksh 4,000 and Ksh 2,500. The program calculates the Net Present Value (NPV) by discounting the cash flows at an estimated interest rate. Both methods are then used to find the rate at which the NPV becomes zero.

**Original output:**

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method:  11.542461%
NPV at Newton solution:   0.000000
Newton iterations: 4
Secant iterations: 7
```

Both methods gave the same IRR of 11.542461%. The NPV was approximately zero, showing that the calculated rate satisfies the investment equation.

## 2. Parameter Change and Results

I changed the annual cash inflows to lower amounts. The original amounts of Ksh 3,000, Ksh 3,500, Ksh 4,000 and Ksh 2,500 were changed to Ksh 2,000, Ksh 3,000, Ksh 3,500 and Ksh 2,500. The initial investment remained Ksh 10,000.

**Modified output:**

```text
IRR using Newton-Raphson: 3.776340%
IRR using Secant method:  3.776340%
NPV at Newton solution:   -0.000000
Newton iterations: 5
Secant iterations: 6
```

After reducing the cash inflows, the IRR decreased from 11.542461% to 3.776340%. This shows that reducing the expected income from an investment also lowers its rate of return. Both methods still produced the same result, and the NPV remained approximately zero.

## 3. Explanation of Output

The results show that both Newton-Raphson and Secant can successfully find the IRR of an investment. The two methods produced the same answer in both cases, although they took different numbers of iterations.

The NPV values were approximately zero, confirming that the calculated rates satisfy the investment equation. The iteration counts show how many steps each method took to reach the result.

## 4. Related Real-World Case: Calculating Interest on a Microfinance Loan

I modified the program to calculate the monthly interest rate charged on a microfinance loan. This example uses the amount borrowed and the monthly repayments to estimate the interest rate.

### Assumptions

- A borrower receives a loan of Ksh 50,000.
- The loan is repaid in 12 monthly instalments.
- Each monthly instalment is Ksh 4,800.
- Payments are made at the end of each month.
- No additional fees are charged.

### Inputs and Outputs

The program uses Ksh 50,000 as the amount received by the borrower and 12 monthly repayments of Ksh 4,800. Newton-Raphson and Secant are then used to find the monthly interest rate that makes the NPV equal to zero.

**Output:**

```text
Monthly rate (Newton): 2.247028%
Monthly rate (Secant): 2.247028%
Equivalent annual rate: 30.5594%
Total repaid: 57600  Interest paid: 7600
NPV at solution: -0.000000
Newton iterations: 4  Secant iterations: 6
```

### Interpretation

The results show that the monthly interest rate on the loan is approximately 2.247028%, which is equivalent to an annual rate of 30.5594%. The borrower repays a total of Ksh 57,600 over the 12 months. Out of this amount, Ksh 50,000 is the original loan, while Ksh 7,600 is the interest paid.

Both methods produced the same monthly interest rate, and the NPV was approximately zero. This shows how root-finding methods can be used to estimate the interest rate on a real microfinance loan.