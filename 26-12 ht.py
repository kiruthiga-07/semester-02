class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            raise ZeroDivisionError("Division by zero is not allowed...")
        return a/b
def calculate():
    calc=Calculator()
    operations={'+':calc.add,'-':calc.sub,'*':calc.mul,'/':calc.div}

    while True:
        try:
            a=float(input("Enter any number: "))
            b=float(input("Enter any number: "))
        except ValueError:
            print("Invalid input please enter numeric values..")
            continue
        try:
            operation=input("Enter any operations (+,-,/,*exit): ")
            if operation=='exit':
                quit()
            if operation not in operations:
                raise KeyError("invalid operation..Please try again..")
                continue
                
               
            result=operations[operation](a,b)
            print(f"The result is: {result}")
                
        except ZeroDivisionError as ze:
            print(ze)
        except TypeError as te:
            print(te)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(f"An unexcepted error occured: {e}")
calculate()
