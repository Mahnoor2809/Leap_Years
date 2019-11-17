# y=int(input("Enter Year : "))
# if(y % 4 == 0 and (y % 400 == 0 or y % 100 != 0)):
#    print(" true, the year is evenly divided by 4, 400")
# else:
#    print(" false, the year is divided by 100 is not a leap year")


def is_leap(year):
 leap = False
 if(year % 4 == 0 ):
   if(year % 400 == 0 or year % 100 != 0):
     leap = True
     print("This year is Leap Year")
 else:
    leap = False
    print("This year is not a multiple of 4 hence it's not a leap year")
 return leap     
year = int(input("enter year : "))
print(is_leap(year))