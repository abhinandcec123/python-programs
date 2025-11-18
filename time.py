class time:
    def __init__(self,hr,minute,sec):
        self.hr=hr
        self.minute=minute
        self.sec=sec
    def __add__(self,other):
        hr=self.hr+other.hr
        minute=self.minute+other.minute
        sec=self.sec+other.sec
        if minute>60:
            hr+=minute//60
            minute=minute%60
        if sec>60:
            minute+=sec//60
            sec=sec%60

        return hr,minute,sec;

h1=int(input("enter the 1st hr:"))
m1=int(input("enter the 1st minute:"))
s1=int(input("enter the 1st sec:"))
h2=int(input("enter the 2nd hr:"))
m2=int(input("enter the 2nd minute:"))
s2=int(input("enter the 2nd sec:"))
time1=time(h1,m1,s1)
time2=time(h2,m2,s2)

time3=time1+time2
print("time3:",time3)

    
