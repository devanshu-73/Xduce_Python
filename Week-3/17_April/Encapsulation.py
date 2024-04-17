# Encapsulation : wrapping data and the methods that work on data within one unit.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.


class Base:
    def __init__(self):
        self.name = 'Devanshu' 
        self.__accno = 9876543210  # Private Variable  

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Calling private member of base class in derived class: ")
        print(self._Base__accno)  # Name Mangling : Accessing private variable __accno from Base class 

obj1 = Derived()
