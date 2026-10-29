
import numpy as np

# Modified matrix values
A = np.array([[2, 3],
              [4, 5]])

B = np.array([[1, 2],
              [3, 4]])

print("TASK 05: MATRIX OPERATIONS WITH MODIFIED INPUTS")

print("\nModified Matrix A:")
print(A)

print("\nModified Matrix B:")
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
x = np.array([2, 3])

print("\nMatrix-Vector Multiplication (A @ x):")
print(A @ x)
