
### Vector Class

Develop a `Vector` class in Python that can accept any number of parameters, enabling it to perform a variety of vector operations. The class should support the following functionalities through appropriate dunder methods:

1. **Instantiation**: Accepts any number of arguments, representing vector components.
2. **String Representation**: Implements a readable format for printing.
3. **Boolean Evaluation**: Evaluates to `False` if all components are zero; otherwise, evaluates to `True`.
4. **Vector Arithmetic**:
   - **Addition** (`+`): Supports element-wise addition with another `Vector`.
   - **Subtraction** (`-`): Supports element-wise subtraction with another `Vector`.
   - **Multiplication** (`*`): Supports element-wise multiplication with another `Vector`.
5. **Comparison**:
   - **Equality** (`==`): Checks if two vectors have the same components.
6. **Indexing and Slicing**:
   - Supports getting and setting individual components by index.
7. **Length** (`len()`): Returns the number of components in the vector.
8. **Other Operations**:
   - **Absolute Value** (`abs()`): Returns the Euclidean norm of the vector.
   - **Scaling**: Supports multiplication and division of the vector by a scalar.
   - **Negation** (`-Vector`): Returns a vector with each component negated.

#### Example Usage

```python
# Instantiation
v1 = Vector(1, 4, 6)
print(v1)              # Expected Output: Vector(1, 4, 6)

# Boolean Evaluation
bool(v1)               # Expected Output: True
bool(Vector(0, 0))     # Expected Output: False

# Length
len(v1)                # Expected Output: 3

# Indexing and Slicing
v1[1]                  # Expected Output: 4
v1[1] = 10
print(v1)              # Expected Output: Vector(1, 10, 6)

# Vector Arithmetic
v2 = Vector(3, 7, 2)
v1 + v2                # Expected Output: Vector(4, 17, 8)
v1 - v2                # Expected Output: Vector(-2, 3, 4)
v1 * v2                # Expected Output: Vector(3, 70, 12)

# Scalar Multiplication and Division
v1 * 3                 # Expected Output: Vector(3, 30, 18)
v1 / 2                 # Expected Output: Vector(0.5, 5, 3)

# Absolute Value (Norm)
abs(v1)                # Expected Output: √(1^2 + 10^2 + 6^2) = 11.66...

# Equality Comparison
v1 == Vector(1, 10, 6) # Expected Output: True

# Negation
-v1                    # Expected Output: Vector(-1, -10, -6)
```



