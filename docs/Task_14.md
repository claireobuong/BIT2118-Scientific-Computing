# Task 14: Curve Fitting Using SciPy

## 1. Inputs and Mathematical Operations

**Input:** The original program uses data representing the number of concurrent users accessing a server and the corresponding server response time in milliseconds.

- Concurrent users: [50, 100, 150, 200, 250, 300, 350]
- Response time: [82, 95, 115, 145, 185, 238, 305] milliseconds.
- Prediction target: 400 concurrent users.

**Operations:** The program uses the `curve_fit()` function from SciPy's `scipy.optimize` module to fit a quadratic mathematical model to the given data.

The quadratic model is:

\(y=ax^2+bx+c\)

Where:
- \(x\) represents the number of concurrent users.
- \(y\) represents the server response time.
- \(a\), \(b\) and \(c\) are parameters estimated by the curve-fitting method.

The program calculates the Root Mean Square Error (RMSE) to measure how closely the fitted curve matches the actual measurements. It also predicts the server response time at 400 concurrent users and plots the original measurements together with the fitted curve.

## 2. Parameter Change and Results

**Parameter changed:** The input measurements were changed in the modified version to examine how different server response-time data affects the fitted quadratic model and its predictions.

**Original result:**

- Fitted model: \(y=0.002167x^2-0.1345x+85.00\)
- RMSE: 1.55 ms
- Predicted response time at 400 users: 377.86 ms.

**Result after the change:**

- Fitted model: \(y=0.003476x^2-0.5405x+108.57\)
- RMSE: 11.47 ms
- Predicted response time at 400 users: 448.57 ms.

**Explanation:** Changing the input measurements affected the estimated model parameters and the predicted response time. The prediction increased from 377.86 ms to 448.57 ms, indicating that the modified dataset produced a higher estimated server response time at 400 concurrent users.

The RMSE also increased from 1.55 ms to 11.47 ms. This means that the modified fitted curve has a larger average prediction error compared with the original measurements. Therefore, the original model provides a closer fit to its data.

## 3. Explanation of the Output

The program displays the fitted quadratic equation, RMSE and predicted server response time at 400 concurrent users.

The fitted equation describes the relationship between the number of users and server response time. The positive quadratic coefficient indicates that response time increases at an accelerating rate as the number of concurrent users increases.

The RMSE measures the difference between the actual response times and the values predicted by the fitted model. A smaller RMSE indicates a closer fit.

The graph displays the original server measurements as scatter points and the fitted quadratic curve as a line. It helps show how well the mathematical model represents the observed server performance and how response time may increase as more users access the server.

## 4. Related Real-World Case: Predicting Monthly Data Storage Growth

**Assumptions**

The modified program represents an organisation monitoring the growth of its monthly data storage requirements. The organisation uses historical storage measurements to predict future storage needs.

It is assumed that storage usage follows an exponential growth pattern and that the historical trend continues over the forecasting period.

**Input Data**

The program uses historical monthly storage measurements, with the month represented by \(x\) and the storage capacity used, measured in GB, represented by \(y\).

An exponential model is fitted to the data using SciPy's `curve_fit()` function:

\(y=ae^{bx}\)

Where:
- \(a\) represents the estimated initial storage usage.
- \(b\) represents the growth rate.
- \(x\) represents the number of months.
- \(y\) represents the predicted storage usage in GB.

**Output**

- Fitted exponential model: \(y=106.89e^{0.1162x}\)
- Monthly growth rate: 12.32%.
- RMSE: 1.03 GB.
- R²: 0.9996.
- Forecast for month 10: 341.6 GB.
- Forecast for month 12: 430.9 GB.

**Interpretation**

The results show that the organisation's data storage usage is increasing at an estimated monthly growth rate of 12.32%.

The model predicts that storage usage will reach approximately 341.6 GB in month 10 and 430.9 GB in month 12. This information can help the organisation plan for additional storage capacity before running out of space.

The RMSE of 1.03 GB indicates that the model's predictions are close to the historical measurements. The R² value of 0.9996 shows that the fitted model explains almost all the variation in the supplied data.

This demonstrates how curve fitting can be used to analyse historical trends and make predictions that support planning and decision-making.