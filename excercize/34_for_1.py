# write a program to count odd and even number in numeric list 
numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,45,65,23,41,20,50,88,100,77,33]
even_number = 0
odd_number = 0
for num in numeric_list:
    if num % 2 == 0:
        even_number = even_number+ 1
    else:
        odd_number = odd_number+ 1
print("Even numbers count:", even_number)
print("Odd numbers count:", odd_number)
