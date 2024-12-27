class Calculate:
    def calculate_final_price(self,base_price,discount_per,tax_per):
        if base_price<=0 or discount_per<=0 or tax_per<=0:
            raise ValueError ('Amount,discount and tax should be in positive')
        total=base_price-(base_price*(discount_per/100))+(base_price*(tax_per/100))
        print(f"Price:{total:.2f}")
calc=Calculate()        

try:
    base_price=float(input())
    discount_per=float(input())
    tax_per=float(input())
    calc.calculate_final_price(base_price,discount_per,tax_per)
except ValueError as e:
    print(e)
