#write a program to convert given grams into kg and remaining grams

#input : 2500 grams
#output : 2 kg and 500 grams 

weight=input("Enter a weight :")
weight=int(weight)

kg=weight// 1000
gram=weight % 1000

print(kg,"kg",gram,"gram")