class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = rectangle(a, b)
c = int(input("Enter length of rectangle: "))
d = int(input("Enter breadth of rectangle: "))
obj1 = rectangle(c,d)
print("Area of rectangle:", obj.area())

print("Perimeter of rectangle: ",obj.perimeter())
print("Area of  2nd rectangle:", obj1.area())
print("Perimeter of 2nd rectangle: ",obj1.perimeter())
