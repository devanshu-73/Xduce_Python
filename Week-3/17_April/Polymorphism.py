# Polymorphism : means having many forms

# Method Overriding : 
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.speak()  # Op: Dog barks
cat.speak()  # Op: Cat meows





# Method Overloading: Python does not support method overloading 
class Calculation:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

math = Calculation()

print(math.add(2, 3))       # Error: add() missing 1 required positional argument: 'z'
print(math.add(2, 3, 4))    # Output: 9

#

