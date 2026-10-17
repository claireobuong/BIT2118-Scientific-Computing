# Task 02: NumPy Arrays and Numerical Computation
## 1. Inputs and Mathematical Operations

The program uses an array containing 24 hourly temperature readings in degrees Celsius.

NumPy is used to calculate the mean, minimum and maximum temperatures. The program also converts the Celsius readings to Fahrenheit using the formula:

Fahrenheit = (1.8 × Celsius) + 32

## 2. Changing an Input

I changed the first temperature reading from 18.5°C to 23.5°C.
Before the change, the daily mean was 23.12°C. After the change, the mean increased to 23.33°C.

The minimum temperature remained 17.50°C, while the maximum remained 29.40°C. The first Fahrenheit reading increased from 65.3°F to 74.3°F.

This happened because increasing one temperature affected the mean and its Fahrenheit conversion, but it did not change the minimum or maximum values.

## 3. Explanation of the Output
The output shows that NumPy can perform calculations on an array of temperature readings. The mean gives the average temperature, while the minimum and maximum show the lowest and highest readings. The Fahrenheit conversion demonstrates how an operation can be applied to every element in an array without using a loop.

## 4. Related Real-World Case: Monitoring Room Temperatures
### Assumptions
A building manager records the temperature of a computer laboratory every hour for one day. The readings are assumed to be accurate.

### Input Data
The input consists of 24 hourly temperature readings in degrees Celsius.

### Output
The program calculates the average, minimum and maximum temperatures and converts the readings to Fahrenheit.

### Interpretation
The results help the building manager understand the laboratory's temperature throughout the day. The average shows the general temperature, while the minimum and maximum help identify cooler and hotter periods. This information can help the manager decide whether ventilation or cooling is needed.