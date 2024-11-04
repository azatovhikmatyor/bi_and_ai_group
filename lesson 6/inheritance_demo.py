
class A:
    def __init__(self, n='John'):
        self.name = n

    def display(self):
        pass

class B(A):
    def __init__(self, roll):
        self.roll = roll
    

obj = B(23)

print(obj.name)

