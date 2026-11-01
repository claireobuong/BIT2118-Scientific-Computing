
import numpy as np

# Hourly computer laboratory temperature readings in Celsius
temperatures_c = np.array([
    22.5, 23.0, 24.0, 25.5, 27.0, 29.5,
    31.0, 32.5, 33.0, 31.5, 29.0, 27.5
])

# Maximum recommended laboratory temperature
temperature_limit = 30.0

# Calculate temperature statistics
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Identify readings above the temperature limit
high_temperatures = temperatures_c[temperatures_c > temperature_limit]

print("COMPUTER LABORATORY TEMPERATURE REPORT")
print(f"Average temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print(f"Temperature limit: {temperature_limit:.2f} C")
print(f"Number of readings above limit: {len(high_temperatures)}")

if len(high_temperatures) > 0:
    print("Warning: The laboratory may require better cooling.")
    print("Readings above limit:", high_temperatures)
else:
    print("The laboratory temperatures are within the limit.")
