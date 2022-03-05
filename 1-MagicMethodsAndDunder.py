"""
Dunder: doble underscore method (__asasd__)
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        # Python automatically delete the object
        print("Object is being deconstructed!")

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}" 
    
    def __len__(self):
        return (self.x**2 + self.y**2)**(1/2)

    def __call__(self):
        print("Hello! I was called")

#p = Person("Mike", 19)
v1 = Vector(10,20)
v2 = Vector(50, 60)

v3 = v1+v2
v3()
#print(v3, v3.__len__())
