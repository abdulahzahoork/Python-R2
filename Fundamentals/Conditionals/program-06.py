# 10. Leap year checker
# Ask the user for a year and determine whether it is a leap year.
# Hint: A year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.

year = int(input("Enter a year: "))

if (year%400==0 or (year%4==0 and year%100!=0)):
    print("It is a leap year.")
else: 
    print("It is not a leap year.")
