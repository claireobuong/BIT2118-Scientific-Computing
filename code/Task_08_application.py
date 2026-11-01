import numpy as np
import matplotlib.pyplot as plt

# Metal rod divided into 20 interior points (1-D steady-state heat flow)
# Assumptions: no heat loss from the sides, ends held at 0 C and 80 C
n = 20
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n)
b[0] = 0.0      # left end temperature
b[-1] = 80.0    # right end temperature

def jacobi(A, b, tol=1e-6, max_iter=5000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        err = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x_new, errors
        x = x_new

    return x, errors

def gauss_seidel(A, b, tol=1e-6, max_iter=5000):
    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]

        err = np.linalg.norm(x - old, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x, errors

    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))
print("Max error Jacobi vs direct:", np.max(np.abs(x_j - x_exact)))
print("Max error Gauss-Seidel vs direct:", np.max(np.abs(x_gs - x_exact)))

# Calculate the average temperature at the two middle interior points
middle_temperature = (x_exact[9] + x_exact[10]) / 2
print("Average temperature at the middle of rod:", middle_temperature.round(3), "C")

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Rod heat conduction: convergence")
plt.legend()
plt.grid(True)
plt.savefig("docs/images/Task_08_rod_convergence.png", dpi=150)
plt.show()
