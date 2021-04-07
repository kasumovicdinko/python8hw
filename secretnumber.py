secret = 20

guess = int(input("Guess the secret number: "))

if secret == guess:
    print("Congratulations! You guessed it!")
elif secret < guess:
    print("Too high! Guess lower!")
elif secret > guess:
    print("Too low! Guess higher!")