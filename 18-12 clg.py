"""#method overloading
def addition(a,b):
    c=a+b
    print(c)
#addition(3,4)
def addition(a,b,c):
    d=a+b+c
    print(d)
addition(3,4,5)    
#The below line shows error
#addition(3,4)

"""


#operator overloading
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(400)
b2=Book(300)
print("Total Number of pages:",b1+b2)       
        
#
class Addition:
    def add(self,a,b,c=0):
        result=a+b+c
        return result
ad=Addition()
ans=ad.add(5,6)
print(ans)

ans1=ad.add(1,5,6)
print(ans1)

#
class Addition:
    def add(self,a,b,c=None):
        if a!=None and b!=None and c==None:
            result=a+b
            return result
        else:
            result=a+b+c
            return result
ad=Addition()        
print(ad.add(3,4))       
