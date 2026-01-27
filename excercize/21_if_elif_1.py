'''Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
----------------------------------------
'''

sub1=int(input("Enter sub1 mark :"))

sub2=int(input("Enter sub2 mark :"))

sub3=int(input("Enter sub3 mark :"))

sub4=int(input("Enter sub4 mark :"))

sub5=int(input("Enter sub5 mark :"))

total=sub1+sub2+sub3+sub4+sub5
print("5 subject total is :",total)

percentage=total/5
print("percentage is :",percentage )

if percentage>=90:
    Grade = "A+"
elif percentage>=80:
    Grade = "A"
elif percentage>=70:
    Grade = "B"
elif percentage>=60:
    Grade = "C"
elif percentage>=50:
    Grade = "D"
else :
    Grade = "Need to improve"


print(f"Grade is:{Grade}")
