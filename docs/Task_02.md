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

## 4. Original Program Output and Interpretation

### Input Data

The program uses 24 hourly temperature readings in degrees Celsius. These readings are illustrative and are used to demonstrate numerical calculations.

### Output Before the Parameter Change

- Daily mean temperature: 23.12°C
- Minimum temperature: 17.50°C
- Maximum temperature: 29.40°C
- First six Fahrenheit readings: 65.3°F, 64.4°F, 64.04°F, 63.5°F, 64.22°F and 66.2°F.

### Interpretation

The results show the average, lowest and highest temperatures recorded during the day. The Fahrenheit values demonstrate that NumPy can convert multiple temperature readings in a single operation. These calculations provide a useful summary of the temperature data.

## 5. Modified Program: Computer Laboratory Temperature Monitoring

### Assumptions

The program uses 12 sample hourly temperature readings from a computer laboratory. A temperature of 30°C is used as an assumed warning threshold for this exercise. The readings are illustrative and were not collected from an actual laboratory.

### Input Data

The program receives 12 temperature readings in degrees Celsius and a temperature limit of 30°C.

### Mathematical Operations

NumPy calculates the mean, minimum and maximum temperatures. Boolean indexing identifies readings greater than 30°C, and the program counts them to determine whether a warning should be displayed.

### Output

- Average temperature: 28.00°C
- Minimum temperature: 22.50°C
- Maximum temperature: 33.00°C
- Temperature limit: 30.00°C
- Number of readings above the limit: 4
- Readings above the limit: 31.0°C, 32.5°C, 33.0°C and 31.5°C.

### Interpretation

The average temperature was 28.00°C, but four readings exceeded the assumed threshold. The maximum temperature was 33.00°C. These results suggest that the laboratory manager should investigate cooling and ventilation conditions. The program demonstrates how numerical computation can help monitor temperatures and identify readings that exceed a specified limit.
