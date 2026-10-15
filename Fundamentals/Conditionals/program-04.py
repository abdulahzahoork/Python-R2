# 4. Temperature checker
# Ask the user to enter the temperature in Celsius.
# - Above 30: It's hot
# - From 15 to 30, inclusive: The weather is pleasant
# - Below 15: It's cold

temp = int(input("Enter temperature in Celcius: "))

if (temp > 30):
    print("It's hot.")
elif (temp >= 15 and temp <= 30):
    print("The weather is pleasant.")
else: 
    print("It's cold.")