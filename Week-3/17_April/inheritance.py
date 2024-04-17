# Inheritance :  one class derive or inherit the properties from another class

class Car1: # Base|Parent Class
    def __init__(self,a,b): # Dunder/Magic Method Automatically Calls
        self.a = a
        self.b = b

    def add(self):
        return f'Your Sum is {self.a+self.b}'

class Car2(Car1): # Derive|Child Class Car 2 Inheriting Parent Class Car 1
    def __init__(self,a,b,c):
        self.c = c
        super().__init__(a,b) # Super KeyWord For Getting All Parent data
    
    def mul(self):
        return f'Your Multiplication is {self.a*self.c+self.b*self.c}'
    
obj = Car2(1,1,2)
print(obj.add())
print(obj.mul()) 

