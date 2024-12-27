"""
num=int(input())
roman_numerals=[(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                              (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                              (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I") ]
roman_result=""
for value,symbol in roman_numerals:
    while num>=value:#493>400|93>90|3
        roman_result+=symbol#CDXCIII
        num-=value#493-400=93|93-90=3
print(roman_result)    
"""
roman_symbol=input()#CDXCIII
numbers=[("M",1000), ("CM",900), ("D",500), ("CD",400),
                 ("C",100), ("XC",90), ("L",50), ("XL",40),
                ("X",10), ("IX",9), ("V",5), ("IV",4), ("I",1) ]
num_result=0
for symbol,value in numbers:#CDXCIII
    while roman_symbol.startswith(symbol):#CDXCIII--CD (400)|XCIII--XC(90)|III--I(1)|II--I(1)|I--(1)
        num_result+=value#400+90=490|490+1=491|491+1=492|492+1=493
        roman_symbol=roman_symbol[len(symbol):]#CDXCIII|XCIII|III|II|I
print(num_result)   #493
