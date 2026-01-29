'''
write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aquarius: January 20–February 18
    Pisces: February 19–March 20
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
   
    

Find their zodiac signs:
Use the birth day and month to determine each person's zodiac sign
For example: If born on March 15, the zodiac sign is Pisces
Use the same zodiac date ranges as in the previous zodiac exercise
'''

date=int(input("Enter date of birth : "))
month=int(input("Enter birth month : "))

if month==1 and date>=20 or month==2 and date<=18:
    print("Aquarius")
elif month==2 and date>=19 or month==3 and date<=20:
    print("Pisces")
elif month==3 and date>=21 or month==4 and date<=19:
    print("Aries")
elif month==4 and date>=20 or month==5 and date<=20:
    print("Taurus")
elif month==5 and date>=21 or month==6 and date<=21:
    print("Gemini")
elif month==6 and date>=22 or month==7 and date<=22:
    print("Cancer")
elif month==7 and date>=23 or month==8 and date<=22:
    print("Leo")
elif month==8 and date>=23 or month==9 and date<=22:
    print("Virgo")
elif month==9 and date>=23 or month==10 and date<=22:
    print("Libra")
elif month==10 and date>=24 or month==11 and date<=21:
    print("Scorpio")
elif month==11 and date>=22 or month==12 and date<=21:
    print("Sagittarius")
else:
    print("Capricorn")