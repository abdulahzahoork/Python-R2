# 14. Ticket pricing
# Ask the user for their age.
# - Under 5: free ticket
# - 5–12: 100
# - 13–59: 250
# - 60 or above: 150
# Print the ticket price. Decide how you want to handle negative ages as an extra challenge.

age = int(input("Enter your age: "))

if (age>=0 and age< 5):
    print("Free Ticket")
elif(age >=5 and age <= 12):
    print("Ticket price: 100")
elif(age>=13 and age<=59):
    print("Ticket price: 250")
elif(age>=60):
    print("Ticket price: 150")
else:
    print("Please enter a valid age.")