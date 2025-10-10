clrs=[]
count=int(input("enter the number of colors:"))
print("enter the colors:")
for x in range(count):
    color=input()
    clrs.append(color)
print("First Color:" ,clrs[0]," Last Color:",clrs[count-1])
