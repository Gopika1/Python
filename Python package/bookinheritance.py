class publisher:
    def __init__(self):
        self.value = "Inside Parent"
    def title(self):
        print(self.value)
        print("TITLE OF BOOK")
    def author(self):
        print("AUTHOR OF THE BOOK::*********")

class book(publisher):
    def __init__(self):
        self.value = "Inside child"
    def title(self):
        print(self.value)
        print("BOOK NAME is python")

class python(book):
    def price(self):
        print("Price of the book::343")

    def no_of_page(self):
        print("NO_OF_PAGES:1000")


obj=python()
obj.title()
obj.author()
obj.price()
obj.no_of_page()