 # write a program to findout heaviest person from 3 person given weight

person1=int(input("Enter person1 weight :"))
person2=int(input("Enter person2 weight :"))
person3=int(input("Enter person3 weight :"))

if person1==person2==person3 :
    print("All person are same weight ")
else :
        if person1>person2:
              print("person1 have a more weight ")
        elif person2>person3:
              print("person2 have a more weight ")
        else:
              print("person3 have a more weight ")
              