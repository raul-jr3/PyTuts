

# def check_leap_year(year):
#     if year == 1900:
#         print("it is not a leap year")
#
#     elif (year % 4 == 0) and (year % 100 != 0):
#         if (year % 400 == 0):
#             print('{} is not a leap year'.format(year))
#         else:
#             print('{} is a leap year'.format(year))
#
#     else:
#         print('{} not a leap year'.format(year))




def check_leap_year(year):
    if year == 1900:
        print("{} is not a leap year".format(year))

    elif (year % 4 == 0) or (year % 400 == 0):
        if (year % 100 != 0):
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is not a leap year")

check_leap_year(2016)



