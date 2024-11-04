from __future__ import annotations
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other: Vector2D):
        return self.x == other.x and self.y == other.y

    def __add__(self, other: Vector2D):
        return Vector2D(x=self.x + other.x, y=self.y + other.y)

    def __bool__(self):
        return not (self.x == 0 and self.y == 0)

    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))

v1 = Vector2D(2, 3)
v2 = Vector2D(1, 6)

# if v1 == v2:
#     print('Equal')
# else:
#     print('Inequal')

v3 = v1 + v2
# print(v3)

v4 = Vector2D(x=0, y=1)
# print(bool(v4))

v5 = Vector2D(x=3, y=4)
print(len(v5))


class Vector:
    pass


v1 = Vector(1, 3, 4)
v5 = Vector(1, 3, 4)
v2 = Vector(3, 6)
v3 = Vector(5, 3, 7, 1)

bool(Vector(0,0,0)) # False


