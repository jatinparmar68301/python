# write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 


mileage=float(input("Enter car average per litre : "))
distance=930
print("total distance in km is :",distance)
print("petrol price is ", 94.70)

train_ticket=3000
print("train ticket price :",train_ticket)

average=distance/mileage
petrol_price=average* 94.30

print("the total price of fuel is :",petrol_price)

if train_ticket<petrol_price:
    print("the 1st class train is better to trvelling ")
else :
    print("you should travel by own car is good ")