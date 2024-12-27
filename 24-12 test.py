def Calculate_fare(miles,mins,surge):
        if miles<=0 or mins<=0:
            raise ValueError("miles and number should be positive....")
        miles_fare=(1.50*miles)
        mins_fare=(0.25*mins)
        base_fare=2.50
        total_fare=(miles_fare+mins_fare+surge+base_fare)
        print(total_fare)
   
try:
    miles=float(input())
    mins=float(input())
    surge=float(input())
    Calculate_fare(miles,mins,surge)
except ValueError as e:
    print(e)

