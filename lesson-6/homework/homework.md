
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

<hr />

### Console Notebook Application

**Objective**: Create a console-based notebook application in Python that allows users to manage notes. Each note should have an ID, text content, and creation date. Notes should be saved to a file so they persist between application sessions.


#### Requirements

1. **Basic Operations**:
    - **Show All Notes**: Display a list of all notes, showing each note's ID and creation date.
    - **Show Note Details**: Display the details of a specific note by its ID.
    - **Create Note**: Add a new note with text content and automatically generate an ID and creation date.
    - **Update Note**: Edit the text of an existing note by its ID.
    - **Delete Note**: Delete a specific note by its ID.

2. **Note Structure**:
    - Each note should have the following attributes:
      - **ID**: A unique identifier for each note (e.g., an auto-incremented integer or a UUID).
      - **Text**: The content of the note.
      - **Created Date**: The date and time the note was created.

3. **File Storage**:
    - Store notes in a file in JSON format (or another suitable format) so that the notes persist even after the application is closed.
    - When the application starts, load the notes from the file into memory.
    - When any change is made (add, update, or delete a note), save the updated list of notes back to the file.

4. **Menu and Input**:
    - The application should display a simple console menu with options for each of the CRUD operations (Create, Read, Update, Delete).
    - Use functions to handle each operation, making it easier to navigate and maintain the code.
    - The user should be able to exit the application gracefully.

5. **Error Handling**:
    - Add error handling for invalid inputs (e.g., non-existent note IDs).

