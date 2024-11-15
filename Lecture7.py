year = input(int("enter the year:")
             if (year < 2001):
               print ("enter year after 2001")
             else:
              print ("enter year before 2100")

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
