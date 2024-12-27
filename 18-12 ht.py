class Calculator:
    def calculate(self,a=None,b=None,c=None):
        if not all(type(arg) in (int,float) for arg in (a,b,c) if arg is not None):
            raise ValueError("All arguments must be integers or floats.")
        if b is None and c is None:
            return a**2
        elif c is None:
            return a+b
        else:
            return a*b*c
cal=Calculator()
try:
    print(cal.calculate(5))
    print(cal.calculate(3,4))
    print(cal.calculate(2,3,4))
    print(cal.calculate(3,"D",2))
except ValueError as e:
    print(e)
    
