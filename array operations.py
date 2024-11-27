#sales figures
import array as arr
sales_figures=arr.array('i',[1200,1500,1100,1700,1600,1800,1300,1900,1750,1600,1400,1500])
print("sales figure of the 6th employee:",sales_figures[5])

sales_figures.reverse()
print("Reversed_sales_figures:",sales_figures.tolist())

sales_figures.extend([1600,1700])
print("Extended_sales_figures:",sales_figures.tolist())
print()

#scores
import array as arr
scores=arr.array('i',[80,90,70,60,50,55,65,75,85,95])
scores.remove(60)
scores.insert(3,62)
print("higest score=",max(scores))
print("lowest score=",min(scores))
for i in scores:
    print(i,end=" ")
print()

#item prices
import array as arr
prices=arr.array('d',[10.99,5.49,20.00,7.95,12.75])
total=sum(prices)
print(total)

prices.pop(1)
print("prices after removing the 2nd item:",prices.tolist())

new_price=15.30
prices.append(new_price)
print("prices after adding new prices at the end of the list:",prices.tolist())


