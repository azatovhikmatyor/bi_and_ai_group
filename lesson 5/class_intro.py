# Odam - class

# John - object
# Adam - object
# Anna - object


class Person:
    words = "This is Person class"  # class variable
    name = "Person"

    def __init__(
        self, name: str, age: int, email: str = None
    ) -> None:  # This is special method to initialize the object
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):  # this is method
        print(f"My name is {self.name} and I am {self.age} years old")


john = Person(name="John", age=40)
anna = Person(name="Anna", age=70, email="example@email.com")
print(john.name, john.age, john.email)  # instance variable
print(anna.name, anna.age, anna.email)


john.introduce()
