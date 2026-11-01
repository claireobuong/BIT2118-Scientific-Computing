# Task 05: Matrix Algebra and Matrix Operations

## 1. Inputs and Mathematical Operations

The original program uses two 2 × 2 matrices, A and B, together with a vector \(x=[5,6]\).

**Matrix A**

\[
A=\begin{bmatrix}1&2\\3&4\end{bmatrix}
\]

**Matrix B**

\[
B=\begin{bmatrix}5&6\\7&8\end{bmatrix}
\]

Using NumPy, I performed several matrix operations to see how the values change after each calculation.

- **Matrix addition:** This adds the matching elements in the two matrices. The result was `[[6, 8], [10, 12]]`.
- **Matrix multiplication:** This involves multiplying the rows of matrix A by the columns of matrix B. The result was `[[19, 22], [43, 50]]`.
- **Determinant:** The determinant of matrix A was approximately -2. Since the result is not zero, the matrix has an inverse.
- **Matrix inverse:** The program calculated the inverse of matrix A. This is useful in mathematical problems where an inverse matrix is needed to reverse certain operations or solve equations.
- **Matrix-vector multiplication:** Matrix A was multiplied by the vector `[5, 6]`, giving `[17, 39]`.

## 2. Parameter Change and Results

I changed the values in both matrices and used a different vector to see how the results would be affected.

The new matrix A was:

\[
A=\begin{bmatrix}2&3\\4&5\end{bmatrix}
\]

The new matrix B was:

\[
B=\begin{bmatrix}1&2\\3&4\end{bmatrix}
\]

I also changed the vector from `[5, 6]` to `[2, 3]`.

After running the program again, matrix addition gave `[[3, 5], [7, 9]]`, while matrix multiplication gave `[[11, 16], [19, 28]]`. Matrix-vector multiplication produced `[13, 23]`.

The determinant of matrix A remained -2 even after changing its values. This showed that different matrices can have the same determinant. Since the determinant was still non-zero, the new matrix also had an inverse. The inverse itself changed because the elements of matrix A were different.

## 3. Explanation of the Output

The results showed me that changing the values in a matrix affects the outcome of most matrix operations. Addition was straightforward because each element was added to the corresponding element in the other matrix. Multiplication required combining rows and columns, which produced different results from addition.

The determinant was useful for checking whether the matrices had inverses. In both tests, the determinant was non-zero, so the inverse could be calculated.

I also observed that multiplying a matrix by a vector produces a new set of values. NumPy made it easier to perform these calculations without having to work through every step manually.

## 4. Related Real-World Case: Computer Graphics Transformation

**Assumptions**

For the real-world example, I used matrix multiplication to demonstrate how points in a drawing can be rotated on a computer screen. The drawing is represented by three points, and each point is rotated 90 degrees anticlockwise around the origin. The example uses a standard Cartesian coordinate system and does not include any shifting or resizing of the drawing.

**Input Data**

The three original points were:

`[[2, 1], [4, 1], [2, 3]]`

I used the following rotation matrix:

\[
R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}
\]

The program multiplied this matrix by the coordinates of each point to find its new position.

**Output**

After the rotation, the coordinates became:

`[[-1, 2], [-1, 4], [-3, 2]]`

**Interpretation**

The results show that all three points moved to new positions after the rotation. For example, the point `(2, 1)` moved to `(-1, 2)`. The same calculation was applied to the other two points.

This example helped me understand how matrix multiplication can be used in computer graphics to rotate objects. Similar calculations are used in video games, animation, image processing and computer-aided design. Instead of calculating each new position using a separate set of instructions, a transformation matrix can be applied to the coordinates to get the new positions.