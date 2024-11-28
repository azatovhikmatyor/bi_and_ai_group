# Parent Class
# Child Class

# Inheritance - Merosxo'rlik


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    def another_method():
        pass


class Location:
    pass


class Employee(Person):
    def __init__(
        self, name: str, age: int, experience: str = None, workplace: Location = None
    ):
        super().__init__(name, age)
        self.experience = experience
        self.workplace = workplace

    def method1():
        pass


# john = Person('John', 40)
# # print(f"{john.name}, {john.age}")
# john.display()


# emp1 = Employee('Adam', 45)
# emp1.display()
# emp1.another_method()
# emp1.method1()


class Student(Employee):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def abc(self):
        print(super().display())


print(Student.__base__.__base__)
print(Employee.__base__)


# std1 = Student('a', 12)

john = Person("John", 45)
# print(dir(john))

