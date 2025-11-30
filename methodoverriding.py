class publisher:
    def get_publisher(self):
        self.pub=input("publisher:")
    def display_publisher(self):
        print("publisher:",self.pub)

class book(publisher):
    def get_book(self):
        self.title=input("enter title:")
        self.author=input("author:")
    def display(self):
        print("title:",self.title)
        print("author:",self.author)

class python(book):
    def get_python(self):
        self.price=input("enter price of book:")
        self.pages=input("enter no of pages:")
    def display(self):
        super().display()
        print("price of book:",self.price)
        print("no of pages:",self.pages)

b=python()
b.get_publisher()
b.get_book()
b.get_python()

b.display_publisher()
b.display()




