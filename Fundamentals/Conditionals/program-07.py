# 11. ATM withdrawal
# Create a simple ATM program.
# - Start with a balance of 5,000.
# - Ask the user how much money they want to withdraw.
# - If the amount is greater than the balance, print Insufficient balance.
# - If the amount is positive and affordable, print the remaining balance.
# - Otherwise, print Invalid amount.



balance = 5000
amount = int(input("Enter amount to withdraw: "))

if (amount > balance):
    print("Insufficient balance.")
elif(amount>0 and amount <= balance):
    balance -= amount
    print(f"Remaining Balance: {balance}")
else:
    print("Invalid amount")