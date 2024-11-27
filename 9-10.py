
class Student:
    s_name=""
    s_dept=""
s=Student()#object creation -> objectname=classnsme()
s.s_name="kiruhtiga"
s.s_dept="AI"
print(f"Name={s.s_name} \n department={s.s_dept}")

class Student:
    s_name="kiruthiga"
    s_dept="AI"
s=Student()#object creation -> objectname=classnsme()
print(f"Name={s.s_name} \n department={s.s_dept}")

class Student:
    s_name=""
    s_dept=""
s1=Student()#object1
s2=Student()#object2

s1.s_name="Kiruhtiga"
s1.s_dept="AI"

s2.s_name="Hema"
s2.s_dept="MBA"

print(f"Name={s1.s_name} \n department={s1.s_dept}")
print(f"Name={s2.s_name} \n department={s2.s_dept}")
print("\nAssign values based on object2")

class Student:
    name="keerthi"
    dept="AI"

    def display(self):
        print(f"Name={self.name}\n department={self.dept}")
s=Student()#object creation
s.display()#method call
        

class Student:
    def __init__(self,name=""):
        self.name=name
    def display(self):
        print("Name=",self.name)
s=Student("Kiruthiga")
s.display()

class Student:
    def __init__(self,name=""):
        self.name=name
    def display(self):
        print("Name=",self.name)
s_name=input()        
s=Student(s_name)
print("Outside the class")
s.display()

class Student:
    ID=""
    def __init__(self,name=""):
        self.name=name
    def getData(self):
        self.ID=input("Enter ID:")
    def display(self):
        print("Student detail")
        print("Name=",self.name)
        print("ID=",self.ID)
s_name=input("enter the name:")
s=Student(s_name)
s.getData()
s.display()



    

    
