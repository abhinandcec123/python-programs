class publisher:
    def get_publisher(self):
        self.pub=input("publisher:")
    def display_publisher(self):
        print("publisher:",self.pub)

class book(publisher):
    def get_book(self):
        self.title=input("enter title:")
        self.author=input("author:")
    def display_book(self):
        print("title:",self.title)
        print("author:",self.author)

class details(book):
    def get_details(self):
        self.price=input("enter price of book:")
        self.pages=input("enter no of pages:")
    def display_details(self):
        print("price of book:",self.price)
        print("no of pages:",self.pages)

b=details()
b.get_publisher()
b.get_book()
b.get_details()

b.display_publisher()
b.display_book()
b.display_details()




