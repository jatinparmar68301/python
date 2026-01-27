'''
write a program to calculate profit or loss amount or no profit no loss & display it using given purchase & sell price.
input: purchase & sale price 
'''
purchase_price = float(input("Enter purchase price :"))
sale_price = float(input("Enter sale price :"))

difference = sale_price - purchase_price

if difference>0:
    print("profit amount is ",difference)
elif difference<0:
    print("loss amount is",difference)
else:
    print("no profit no loss")
print("Good bye.")