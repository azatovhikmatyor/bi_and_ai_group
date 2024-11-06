class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # private-like attribute

    def getSalary(self):
        return self.__salary


john = Person("John", 25, 40000)
print(john._Person__salary)

