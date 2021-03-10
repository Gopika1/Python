class Publisher:

    def myMethod(self):
        print("About the book")


class Book(Publisher):
    def myMethod(self):
        print("About the book")
        print("Tittle:Python book")
        print("Author:Alexander")


class Python(Book):
    def display(self):
        print("Price:300")
        print("Pages:550")


ob = Python()
ob.myMethod()
ob.display()