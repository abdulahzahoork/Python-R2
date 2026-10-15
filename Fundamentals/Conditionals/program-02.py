# 2. Even or odd
# Ask the user for an integer and determine whether it is even or odd.
# Example input: 7
# Expected output: Odd number

num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("Even number")
else:
    print("Odd number")