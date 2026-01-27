# write a program to findout which is cheaper product for purchase from 2 product's weight and price. 
# also display how much cheaper
# input price and weight of 1st product
# input price and weight of 2nd product

price1 = int(input("Enter 1st product price :"))
weight1 = float(input("Enter 1st product weight :"))

price2 = int(input("Enter 2nd product price :"))
weight2 = float(input("Enter 2nd product weight :"))

price_per_gram_1 = price1 / weight1
price_per_gram_2 = price2 / weight2

if price_per_gram_1<price_per_gram_2:
    print('1st product is cheaper then 2nd product')
    print(price_per_gram_2 - price_per_gram_1, " is cheaper per gram")
else:
    print('2nd product is cheapter then 1st product')
    print(price_per_gram_1 - price_per_gram_2, " is cheaper per gram")