# Task 02: NumPy Arrays and Numerical Computation

## 1. Inputs and Mathematical Operations

The original program uses an array containing 24 hourly temperature readings in degrees Celsius. NumPy is used to calculate the mean, minimum and maximum temperatures.

The program also converts Celsius temperatures to Fahrenheit using the formula:

**Fahrenheit = (1.8 × Celsius) + 32**

These operations demonstrate how NumPy can perform numerical calculations and apply mathematical operations to an entire array without using a loop.

## 2. Changing an Input

To test how changing an input affects the results, I created a separate program named `Task_02_modified_input.py`. I changed the first temperature reading from 18.5°C to 23.5°C while keeping all other readings unchanged.

### Original Output

- Daily mean temperature: 23.12°C
- Minimum temperature: 17.50°C
- Maximum temperature: 29.40°C
- First Fahrenheit reading: 65.3°F

### Modified Output

- Daily mean temperature: 23.33°C
- Minimum temperature: 17.50°C
- Maximum temperature: 29.40°C
- First Fahrenheit reading: 74.3°F

### Interpretation

Increasing the first temperature reading by 5°C increased the daily mean from 23.12°C to 23.33°C. The minimum and maximum temperatures remained unchanged because the modified reading did not exceed the existing minimum or maximum. The first Fahrenheit reading increased from 65.3°F to 74.3°F because the Celsius-to-Fahrenheit conversion was applied to the changed value.

This experiment demonstrates how changing one input can affect some calculated results while leaving others unchanged.

## 3. Explanation of the Original Output

The mean represents the average of the 24 hourly temperature readings. The minimum identifies the lowest reading, while the maximum identifies the highest reading.

The Fahrenheit values demonstrate vectorized computation, where NumPy applies the conversion formula to every element in the array without requiring a loop.

The original output is saved in `docs/outputs/Task_02_original_output.txt`, while the modified-input output is saved in `docs/outputs/Task_02_modified_output.txt`.

## 4. Modified Program: Computer Laboratory Temperature Monitoring

### Assumptions

The modified program uses 12 illustrative hourly temperature readings from a computer laboratory. A temperature of 30°C is used as an assumed warning threshold for this exercise. The readings were not collected from an actual laboratory, and the threshold is an assumption for the demonstration.

### Input Data

The program receives 12 temperature readings in degrees Celsius and a temperature limit of 30°C.

### Mathematical Operations

NumPy calculates the mean, minimum and maximum temperatures. Boolean indexing identifies readings greater than 30°C, and the program counts these readings to determine whether a warning should be displayed.

### Output

- Average temperature: 28.00°C
- Minimum temperature: 22.50°C
- Maximum temperature: 33.00°C
- Temperature limit: 30.00°C
- Number of readings above the limit: 4
- Readings above the limit: 31.0°C, 32.5°C, 33.0°C and 31.5°C

The real-world program output is saved in `docs/outputs/Task_02_lab_temperature_output.txt`.

### Interpretation

Although the average laboratory temperature was 28.00°C, four readings exceeded the assumed threshold, and the maximum reached 33.00°C. These results suggest that the laboratory manager should investigate cooling and ventilation conditions.

The program demonstrates how numerical computation and conditional checks can be used to monitor temperatures and identify readings that exceed a specified limit.

## 5. Conclusion

Task 02 demonstrates the use of NumPy arrays, statistical calculations, vectorized operations and Boolean indexing. The input-change experiment shows how changing one temperature affects the mean and its Fahrenheit conversion. The computer-laboratory example demonstrates how the same techniques can be adapted to a related practical problem.