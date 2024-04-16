# OOP Stands For Object Oriented Programming
# Key Points : 
#            1) Class & Object 
#            2) Inheritance  
#            3) Encapsulation  
#            4) Polymorphism

# Sample

class Student: # Student Class Created

    # Data Members
    name = 'Devanshu'
    standard = 10

    # Member Function
    def Display(self):
        return f'{self.name} is in the {self.standard}th standard' 

std1 = Student() # Student Class Object 

print(std1.Display()) # Printing Output of Member Fun Using Object


# Example 1 :

class Car1:
    def __init__(self,a,b): # Dunder/Magic Method Automatically Calls
        self.a = a
        self.b = b

    def add(self):
        return f'Your Sum is {self.a+self.b}'

class Car2(Car1):
    def __init__(self,a,b,c):
        self.c = c
        super().__init__(a,b) # Super KeyWord For Getting All Parent data

    def mul(self):
        return f'Your Multiplication is {self.a*self.c+self.b*self.c}'

obj = Car2(1,1,2)
print(obj.add())
print(obj.mul()) 