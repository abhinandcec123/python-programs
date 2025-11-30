class Rectangle:
    def __init__(self, length, width):
        self.__length = length     
        self.__width = width       

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


r1 = Rectangle(10, 5)
r2 = Rectangle(8, 8)

if r1 < r2:
    print("Rectangle r1 has smaller area than r2")
else:
    print("Rectangle r1 has larger or equal area than r2")
