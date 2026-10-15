# Guess the number
# Choose a secret number, such as 7. Keep asking the user to guess until they get it right.
# Hint: Use while and if/else.

secret_num = 7


while(True):
    guess = int(input("Guess the secret number: "))
    if (guess == secret_num):
        print("You Win!")
        break
    else:
        print("Wrong! Try again.")