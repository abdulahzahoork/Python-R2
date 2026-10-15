# 1. Positive, negative, or zero
# Ask the user to enter a number. Print whether it is positive, negative, or zero.
# Example input: -5
# Expected output: The number is negative


num = int(input("Enter a number: "))

if (num == 0):
    print("The number is zero.")
elif (num > 0):
    print("The number is positive.")
else:
    print("The number is negative.")