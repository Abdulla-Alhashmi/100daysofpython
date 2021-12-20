print("Find out if a year is a leap year or not! \n")
year = int(input("type the year you want to invistigate "))
if year % 4 == 0:
    if (year % 100) == 0 :
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("Not a leap year")
    else:
        print("This is a leap year")
else:
    print("Not a leap year")

    

    

