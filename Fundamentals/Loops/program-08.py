# Number guessing hints: Extend the guessing game to print "Too high!" or "Too low!" after each incorrect guess.

print("Guess the secret number!")

while(True):
    guess = int(input("Take a guess: "))

    if (guess > 7):
        print("Too High")
    elif(guess <7):
        print("Too Low")
    else:
        print("You Win!")
        break