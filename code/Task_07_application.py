import numpy as np
import timeit
from scipy.linalg import lu_factor, lu_solve

# Thermal network of 4 rooms. Same coefficient matrix A (heat-flow
# coupling), but heat input b changes every hour for 24 hours.
# Assumptions: steady state each hour, A is fixed (building does not change)
A = np.array([
    [ 5., -1.,  0., -1.],
    [-1.,  5., -1.,  0.],
    [ 0., -1.,  5., -1.],
    [-1.,  0., -1.,  5.]
])
rng = np.random.default_rng(7)
b_all = rng.uniform(10, 40, size=(24, 4))   # 24 hourly heat inputs

lu, piv = lu_factor(A)
temps = np.array([lu_solve((lu, piv), b) for b in b_all])

print("Room temperatures at hour 0:", temps[0])
print("Room temperatures at hour 23:", temps[23])
print("Hottest room-hour:", temps.max().round(3))
print("Max residual over all hours:",
      np.max(np.abs(b_all - temps @ A.T)))

# Timing: 20000 right-hand sides
B = rng.uniform(10, 40, size=(20000, 4))
def with_lu():
    for b in B:
        lu_solve((lu, piv), b)
def with_solve():
    for b in B:
        np.linalg.solve(A, b)
print(f"lu_solve x20000: {timeit.timeit(with_lu, number=1):.3f} s")
print(f"np.linalg.solve x20000: {timeit.timeit(with_solve, number=1):.3f} s")
