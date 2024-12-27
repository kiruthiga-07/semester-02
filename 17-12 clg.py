class Library:
    def issue_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
class DigitalLibrary:
    def issue_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
lib=Library()
dig=DigitalLibrary()

book=input("Enter the book name: ")
username=input("Enter the user name: ")

print(lib.issue_book(book,username))
print(lib.return_book(book,username))

print(dig.issue_book(book,username))
print(dig.return_book(book,username))
