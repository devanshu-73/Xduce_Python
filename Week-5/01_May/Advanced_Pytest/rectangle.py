class Rectangle:

    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)