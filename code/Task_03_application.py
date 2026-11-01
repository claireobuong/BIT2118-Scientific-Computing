
import numpy as np
import timeit

# Simulated network latency readings in milliseconds
# This example represents a network administrator monitoring a connection.
rng = np.random.default_rng(10)
latency_ms = rng.uniform(5, 250, 100_000)

# Assumed maximum acceptable network latency in milliseconds
latency_limit = 150.0


def loop_version():
    squared_latency = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared_latency.append(seconds ** 2)
    return squared_latency


def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2


# Calculate squared latency using NumPy vectorization
squared_latency = vectorized_version()

# Identify readings above the assumed latency limit
high_latency = latency_ms[latency_ms > latency_limit]

# Measure vectorized execution time
vector_time = timeit.timeit(vectorized_version, number=3) / 3

print("NETWORK LATENCY MONITORING REPORT")
print(f"Number of readings: {len(latency_ms):,}")
print(f"Average latency: {np.mean(latency_ms):.2f} ms")
print(f"Minimum latency: {np.min(latency_ms):.2f} ms")
print(f"Maximum latency: {np.max(latency_ms):.2f} ms")
print(f"Assumed latency limit: {latency_limit:.2f} ms")
print(f"Readings above the limit: {len(high_latency)}")
print(f"Average squared latency: {np.mean(squared_latency):.6f} squared seconds")
print(f"NumPy vectorized execution time: {vector_time:.6f} seconds")

if len(high_latency) > 0:
    print("Warning: Some network latency readings exceed the assumed limit.")
else:
    print("All network latency readings are within the assumed limit.")
