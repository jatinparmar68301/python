# write a program to findout most young person from 4 person given age

person1=int(input("Enter person1 age :"))
person2=int(input("Enter person2 age :"))
person3=int(input("Enter person3 age :"))
person4=int(input("Enter person4 age :"))

if person1==person2==person3==person4:
    print("All person are same age")
else :
        if person1>person2:
              print("person1 have a most young person ")
        elif person2>person3:
              print("person2 have a most young person ")
        elif person3>person4:
               print("person2 have a most young person ")
        else:
              print("person4 have a most young person ")