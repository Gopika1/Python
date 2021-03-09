class Student:
  def __init__(self, Name, Mark,Branch):
    self.Name = Name
    self.Mark = Mark
    self.Branch = Branch

  def display(self):
    print(" My Name is " , self.Name, "and my mark is " ,self.Mark, "and my branch is " ,self.Branch)
  def __del__(self):
        print("Destructor called")

p1 = Student("John", 36,"MCA")
p2 = Student("Malu", 42,"MCA")
p1.display()
p2.display()
del p2
p2.display()