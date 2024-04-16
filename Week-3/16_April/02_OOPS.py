class Car1:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return f'Your Sum is {self.a+self.b}'

class Car2(Car1):
    def __init__(self,a,b,c):
        self.c = c
        super().__init__(a,b)

    def mul(self):
        return f'Your Multiplication is {self.a*self.c+self.b*self.c}'

obj = Car2(1,1,2)
print(obj.add())
print(obj.mul())