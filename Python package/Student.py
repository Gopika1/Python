class Student:
    def __init__(self, Name, Mark, Branch):
        self.Name = Name
        self.Mark = Mark
        self.Branch = Branch


    def display(self):
     print(" My Name is " + self.Name, "and my mark is " + self.Mark, "and my branch is " + self.Branch)


n = input("Enter a name")
m = input("Enter a mark")
b = input("Enter the branch")
n1 = input("Enter a name")
m1 = input("Enter a mark")
b1 = input("Enter the branch")

p1 = Student(n,m,b)
p2 = Student(n1,m1,b1)
p1.display()
p2.display()
del p2.Branch
print(p2.branch)