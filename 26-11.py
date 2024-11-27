"""
#parametarised
class Library:
    def __init__(self,book,author):
        self.book=book
        self.author=author

    def show(self):
        print(f"Book:{self.book}\nAuthor:{self.author}")

s=Library("Harry Potter","J.K.Rowling")
s.show()

#non-parametarised
class Library:
    def __init__(self):
        self.book="Harry potter"
        self.author="J.K.Rowling"

    def show(self):
        print(f"Book:{self.book}\nAuthor:{self.author}")

s=Library()
s.show()

#para and non-para mixed
class Library:
    def __init__(self,book,author="J.K.Rowling",published=1997):
        self.book=book
        self.author=author
        self.published=published

    def show(self):
        print(f"Book:{self.book}\nAuthor:{self.author}\nPublished:{self.published}")

s=Library("Harry Potter")
s.show()
"""
