#write a program to display only positive value from the numeric list using for loop
list = [12, -45, 7, -3, 89, -22, 0, 34, -9, 56,100,145,-5,500] #Array
#task count no of positive & negative values and display it after for loop finish
for item in list:
    if item>0:
        print(item,end=' ') # 12 -45 7 

print() #new line
print("Good bye")

print("----------------------------------------------------")

#task-: count no of positive & negative values and display it after for loop finish

positive = 0
negative = 0

print("positive value's are :",end=' ')
for item in list:
    if item>0:
        positive = positive+1
        print(item,end=' ') 

print() #new line
print("positive count =",positive)

print("negative value's are :",end=' ')
for item_2 in list:
    if item_2<0:
        negative = negative+1
        print(item_2,end=' ')

print()
print("negative count =",negative)
print("Good bye")
