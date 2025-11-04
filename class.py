class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

l=int(input("enter length of first rect:"))
b=int(input("enter breadth of first rect:"))
r1=rectangle(l,b)
print('perimeter:',r1.perimeter())
print('Area:',r1.area())

l=int(input("enter length of second rect:",))
b=int(input("enter breadth of second rect:"))
r2=rectangle(l,b)
print('perimeter:',r2.perimeter())
print('Area:',r2.area())

if r1.area()>r2.area():
    print("rectangle 1 is greater")
else:
    print("rectangle 2 is greater")
