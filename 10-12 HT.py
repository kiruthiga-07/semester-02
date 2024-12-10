#1
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_features(self):
        print(f"Make:{self.make}\nModel:{self.model}\nYear:{self.year}")

class Car(Vehicle):
    def __init__(self,make,model,year,doors,trunk_capacity):
        Vehicle.__init__(self,make,model,year)
        self.doors=doors
        self.trunk_capacity=trunk_capacity
    def display_features(self):
        super().display_features()
        print(f"Doors:{self.doors}\nTrunk capacity:{self.trunk_capacity}")
        
class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity,axles):
        Vehicle.__init__(self,make,model,year)
        self.cargo_capacity=cargo_capacity
        self.axles=axles
    def display_features(self):    
        super().display_features()
        print(f"Cargo capacity:{self.cargo_capacity}\nAxles:{self.axles}")

class PickupTruck(Car,Truck):
    def __init__(self,make,model,year,doors,trunk_capacity,cargo_capacity,axles):
         Car.__init__(self,make,model,year,doors,trunk_capacity)
         Truck.__init__(self,make,model,year,cargo_capacity,axles)
    def display_features(self):
        print("Pickup Truck Features:")
        super().display_features()
        
pickup=PickupTruck("Tesla","Tesla Model 5",2024,4,500,2.5,2)
pickup.display_features()
print("------------------------------------------")

#2
class Product:
    def __init__(self,pro_id,name,price):
        self.pro_id=pro_id
        self.name=name
        self.price=price
    def displayinfo(self):
        print(f"Product ID: {self.pro_id}\nProduct Name: {self.name}\nProduct Price: {self.price}")
        
class Electronics(Product):
    def __init__(self,pro_id,name,price,warranty,brand):
        Product.__init__(self,pro_id,name,price)
        self.warranty=warranty
        self.brand=brand
    def displayElectronics(self):
        self.displayinfo()
        print(f"Warranty Period for Product is: {self.warranty}\nProduct Brand: {self.brand}")
        
class Clothing(Product):
    def __init__(self,pro_id,name,price,size,material):
        Product.__init__(self,pro_id,name,price)
        self.size=size
        self.material=material
    def displayClothing(self):
        super().displayinfo()
        print(f"Cloth Size: {self.size}\nCloth Material: {self.material}")
        
e=Electronics("k6789","Mobile",13000,"1 year","POCO")
e.displayElectronics()
print()
c=Clothing("k6789","Dress",400,"M","cotton")
c.displayClothing()
        
        
