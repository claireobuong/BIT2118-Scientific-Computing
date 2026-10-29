
import numpy as np

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("TASK 05: MATRIX ALGEBRA AND MATRIX OPERATIONS")
print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix addition
print("\nMatrix Addition (A + B):")
print(A + B)

# Matrix multiplication
print("\nMatrix Multiplication (A @ B):")
print(A @ B)

# Determinant of matrix A
print("\nDeterminant of Matrix A:")
print(np.linalg.det(A))

# Inverse of matrix A
print("\nInverse of Matrix A:")
print(np.linalg.inv(A))

# Multiply matrix A by a vector
x = np.array([5, 6])

print("\nMatrix-Vector Multiplication (A @ x):")
print(A @ x)
