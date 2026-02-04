# write a program to generate and display sum of all the float values in tuple and also calculate average

tuple = (1.5, 2.3, 3.7, 4.0, 5.6, 6.2, 7.8, 8.4, 9.9, 10.1)
sum = 0.0
for value in tuple:
    sum = sum + value
average = sum / len(tuple)
print("Sum of all float values:",sum)
print("Average of float values:", average)