
"""
#non para
class Student:
    def __init__(self):
        self.name='kiruthiga'
        self.dept='AI'
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
stu=Student()
stu.display()


class Library:
    def __init__(self):
        self.book_name="Harry potter"
        self.author_name="j.k. Rowling"
    def getbookdetails(self):
        print(f"Book Name:{self.book_name}\nAuthor Name:{self.author_name}")
lib=Library()
lib.getbookdetails()
"""
#parameterised
class Student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def display(self):
        print(f"Name:{self.name}\nDepartment:{self.dept}")
stu=Student('kiruthiga','AI')
stu.display()





        
