
import numpy as np

print("TASK 05: REAL-WORLD APPLICATION - COMPUTER GRAPHICS")

# Coordinates of three points in a simple drawing
points = np.array([
    [2, 1],
    [4, 1],
    [2, 3]
])

# Transformation matrix for a 90-degree anticlockwise rotation
rotation_matrix = np.array([
    [0, -1],
    [1,  0]
])

print("\nOriginal coordinates:")
print(points)

print("\nRotation matrix:")
print(rotation_matrix)

# Transpose points so the transformation can be applied
rotated_points = (rotation_matrix @ points.T).T

print("\nCoordinates after 90-degree anticlockwise rotation:")
print(rotated_points)
