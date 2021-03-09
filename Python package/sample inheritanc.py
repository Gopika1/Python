class Employer:


  def __init__(self):
    print("Calling parent constructor")


  def EmployerMethod(self):
    print("Hi,I am an Employer")

class Employee(Employer):

    def __init__(self):
        print("Calling Child constructor")
    def EmployeeMethod(self):
        print("Hi,I am an employee from CS dept")

Emp = Employee()
Emp.EmployeeMethod()
Emp.EmployerMethod()