#multiple inheritance
class Employee:
    def __init__(self,name,ID,position):
        self.name=name
        self.ID=ID
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nID:{self.ID}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayAddressInfo(self):
        print(f"Street:{self.street}\nState:{self.state}\nCountry:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,ID,position,street,state,country):
        super().__init__(name,ID,position)
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayAddressInfo()
ed=EmployeeDetails("Kiruthiga",21,"Manager","shenoy Nagar","Tamil nadu","India")
ed.displayEmp()
            
        
