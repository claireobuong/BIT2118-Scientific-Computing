
import numpy as np
import timeit

# Simulated network latency readings in milliseconds
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 100_000)


def loop_version():
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared


def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2


# Measure execution time
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

# Calculate the vectorized result
result = vectorized_version()

print("TASK 03: NUMPY VECTORIZATION")
print(f"Number of latency readings: {len(latency_ms):,}")
print(f"First five latency readings (ms): {latency_ms[:5]}")
print(f"First five squared values (squared seconds): {result[:5]}")
print(f"Python loop execution time: {loop_time:.6f} seconds")
print(f"NumPy vectorized execution time: {vector_time:.6f} seconds")

if vector_time > 0:
    print(f"Speed improvement: {loop_time / vector_time:.2f} times faster")
