def display_books(books):
       for i in books:
               print(i,end=" ")
n=int(input()) 
books=[] 
for _ in range(n): 
    m=input() 
    books.append(m) 
display_books(books) 
print() 
 
def add_books(books): 
    a=int(input()) 
    for i in range(a): 
        newbook=input("Enter the book to add:") 
        books.append(newbook) 
    print("\nbooks after added new books") 
    print(books) 
add_books(books) 
print() 
 
def remove_book(books): 
    books_remove=input("Enter the book to remove: ") 
    if books_remove in books: 
        books.remove(books_remove) 
    else: 
        print("Book not found") 
    print("After removing books") 
    print(books) 
remove_book(books)

