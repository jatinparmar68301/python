# write a program to count digits in given string 
string = "Hello123 Everyone45 MY67 name89 is0 Jattu Parmar."
digit = 0
for char in string:
    if char.isdigit():
        digit = digit+1 
print("Total number of digits in the string:", digit)
