n=int(input("enter the limit:"))
a,b=0,1
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
