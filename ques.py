
#------------------------------------------------
# boolean true/ false then explain ur answer
#------------------------------------------------
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) != 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
#---------------------------------------------------
  
def is_leap (year):
    # print(year)
    if (year %4 == 0 or year % 400== 0):
        print(" true, the year is evenly divided by 4, 400")
    elif (year % 100 == 0):
        print(" false, the year is divided by 100 is not a leap year")
    # return year

years = int(input("enter the year :"))
is_leap(years)
#----------------------------------------------------------------------------

# year = int(input("Enter a year: "))

# if (year % 4 ==0 and year % 400 ==0 and year % 100 != 0):
#     print("{0} is a leap year".format(year)) 
# else:
#     print("{0} is not a leap year".format(year))   