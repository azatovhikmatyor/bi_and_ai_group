1. **Create an array with all zeros, size 10, and set the fifth element to 1.**
   Expected output:
    ```python
    >>> array([0., 0., 0., 0., 1., 0., 0., 0., 0., 0.])
    ```

2. **Create an array with values ranging from 10 to 49.**
   Expected output:

   ```python
   >>> array([10, 11, 12, ..., 47, 48, 49])
   ```

3. **Reverse the array you created in the previous step.**
   Expected output:

   ```python
   >>> array([49, 48, 47, ..., 12, 11, 10])
   ```

4. **Create a 3x3 matrix with values ranging from 0 to 8.**
   Expected output:

   ```python
   >>> array([[0, 1, 2],
   ...        [3, 4, 5],
   ...        [6, 7, 8]])
   ```

5. **Find the indices of all non-zero elements in the array `[1, 2, 0, 0, 4, 0]`.**
   Expected output:

   ```python
   >>> array([0, 1, 4])
   ```

6. **Create a 3x3 identity matrix.**
   Expected output:

   ```python
   >>> array([[1., 0., 0.],
   ...        [0., 1., 0.],
   ...        [0., 0., 1.]])
   ```

7. **Create a random 3x3 matrix and find the minimum and maximum values.**

   ```python
   # Expected output: minimum and maximum values of the random matrix
   ```

8. **Normalize a 5x5 random matrix so that the values are between 0 and 1.**

   ```python
   # Expected output: normalized matrix where all values are between 0 and 1
   ```

9. **Find the closest value in an array to a given number.**
   Given array:

   ```python
   array = np.array([1, 3, 5, 11, 15, 20, 25])
   target = 14
   ```

   **Goal:** Find the value in `array` that is closest to `target`.

10. **Replace the maximum element in each row of a 2D array with 0.**
    Given array:

    ```python
    array = np.array([[5, 9, 3], [10, 2, 15], [6, 7, 8]])
    ```

    **Goal:** Replace the maximum value in each row with 0.

11. **Find the most common value in an array.**
    Given array:

    ```python
    array = np.array([2, 3, 2, 5, 8, 3, 3, 7, 2, 3, 5, 5, 5, 5])
    ```

    **Goal:** Find the value that appears most frequently in the array. (If there’s a tie, return any one of them.)

12. **Compute the matrix product of a 2D array and its transpose.**
    Given array:

    ```python
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ```

    **Goal:** Find the matrix product of `array` and its transpose.

13. **Calculate the determinant of a 3x3 matrix.**
    Given matrix:

    ```python
    matrix = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    ```

    **Goal:** Compute the determinant of `matrix`.

14. **Find the inverse of a matrix (if it exists).**
    Given matrix:
    ```python
    matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    ```
    **Goal:** Calculate the inverse of `matrix`. If the matrix is singular (non-invertible), return a message indicating so.
