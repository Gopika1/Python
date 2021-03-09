class Rectangle:
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length  = length
    def area(self):
        return self.breadth * self.length

    def __lt__(self, other):
        return self.rect1 < other.rect2
print("Rectangle 1")
a = int(input("enter the length: "))
b = int(input("enter the breadth: "))
obj1 = Rectangle(a,b)
print("Area of the Rectangle 1 : ",obj1.area())
print("Rectangle 2")
a = int(input("enter the length: "))
b = int(input("enter the breadth: "))
obj2 = Rectangle(a,b)
print("Area of the Rectangle 2: ",obj2.area())
rect1 = obj1.area()
rect2 = obj2.area()

r.__lt__(rect1,rect2)
