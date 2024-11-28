# dunder methods = double underscore methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


p1 = Person("Josh", 40)
p2 = Person("Josh", 40)

print(p1 == p2)


