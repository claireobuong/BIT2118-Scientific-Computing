# Task 03: NumPy Vectorization

## 1. Inputs and Mathematical Operations
**Input**: The original program generates 1,000,000 simulated network latency readings between 5 and 250 milliseconds using NumPy.
**Operations**: Each reading is converted from milliseconds to seconds and then squared. The program performs the same calculation using a Python loop and NumPy vectorization.
**Performance measurement**: The timeit module measures how long each approach takes. The results are used to compare their execution speeds.

## 2. Parameter Change and Results
**Parameter changed** : The number of latency readings was reduced from 1,000,000 to 100,000 in a separate copy of the original program.
Original result: The Python loop took 0.580468 seconds, while NumPy vectorization took 0.005154 seconds. In this run, NumPy was 112.62 times faster.
**Result after the change**: With 100,000 readings, the Python loop took 0.041714 seconds, while NumPy vectorization took 0.001015 seconds. NumPy was 41.11 times faster in this run.
**Explanation**: Both approaches took less time when the number of readings was reduced because there were fewer values to process. NumPy was faster in both cases. The speed difference was not the same in each run because execution times can vary depending on the computer and its current workload.

## 3. Explanation of the Output
The program displays the total number of readings, the first five latency values, their squared values in seconds, and the execution time for each approach.
The results show that NumPy vectorization can process large arrays much faster than a traditional Python loop. Instead of processing each value through an explicit Python loop, NumPy applies the calculation to the array directly.

## 4. Related Real-World Case: Network Latency Monitoring
**Assumptions**
The modified program represents a network administrator checking the response times of a network connection. It uses simulated readings rather than measurements from a real network. A limit of 150 milliseconds is assumed for identifying readings that may need further investigation. This limit is used for the assignment example and is not a universal standard.

## Input Data
The program generates 100,000 latency readings ranging from 5 to 250 milliseconds. It calculates the average, minimum, and maximum latency, as well as the average squared latency in seconds. It also counts the readings that exceed the assumed 150-millisecond limit.

## Output
•	Number of readings: 100,000
•	Average latency: 127.46 milliseconds
•	Minimum latency: 5.00 milliseconds
•	Maximum latency: 249.99 milliseconds
•	Assumed latency limit: 150.00 milliseconds
•	Readings above the limit: 40,640
•	Average squared latency: 0.021224 squared seconds
•	NumPy vectorized execution time: 0.000759 seconds

## Interpretation
The average latency was 127.46 milliseconds, which is below the assumed limit of 150 milliseconds. However, 40,640 readings exceeded that limit. This shows that even when the average is within the chosen limit, some individual readings may still be high.

A network administrator could investigate these readings to determine whether there are delays that need attention. The program demonstrates how NumPy can process many readings quickly and identify values above a specified limit. Since the readings are simulated, the results do not describe the performance of an actual network connection.

