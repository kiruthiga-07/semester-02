#1
library=[]
def display_books():
    if library:
        print("available books:")
        for book in library:
            print(f"- {book}")
    else:
        print("no books are available in the library.")

def add_book(book):
        library.append(book)
        print(f'"{book}" has been added to the library.')

def remove_book(book):
    if book in library:
        library.remove(book)
        print(f'"{book}" has been removed from the library.')
    else:
        print(f'"{book}" not found in the library.')

display_books ()
add_book("harry potter")
add_book("tangled")
display_books()
remove_book("tangled")
display_books()
print()

#2
inventory={}
def view_inventory():
    if inventory:
        print("current inventory:")
        for product,quantity in inventory.items():
            print(f"{product}:{quantity}")
    else:
        print("inventory is empty.")

def add_product(product,quantity):
    if product in inventory:
        inventory[product]+=quantity
    else:
        inventory[product]=quantity
    print(f"added {quantity} of {product} to the inventory.")

def remove_product(product):
    if product in inventory:
        del inventory[product]
        print(f"removed {product} from the inventory.")
    else:    
        print(f"{product} does not exist in the inventory.")

add_product("apples", 50)
add_product("bananas", 30)
view_inventory()
remove_product("bananas")
view_inventory()
remove_product("oranges")

