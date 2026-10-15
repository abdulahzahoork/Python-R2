# Factorial: Ask for a number and calculate its factorial. For example, 5! = 120.

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print(f"Factorial: {fact}")
