#write  a program to find out whether given year is millennium year or not. using if else decision making statements.

year = int(input("Enter a year: "))

if year % 1000 == 0:
    print(year, "is a Millennium Year")
else:
    print(year, "is not a Millennium Year")
