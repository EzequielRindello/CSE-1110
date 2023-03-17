import random
""" Selec a random number to the user to guess"""
number_to_guess = random.randrange(0, 10)
guess_count = 0
guess = 0
print("Try to guess between 0 and 10! ")
while number_to_guess != guess:
    try:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low")
            guess_count = guess_count + 1
        elif guess > number_to_guess:
            print("Too high!")
            guess_count = guess_count + 1
    except:
        print("Error. Please enter an integer.")
guess_count = guess_count + 1
print("-----------------------------------------------------------")
print(f"You guessed it right!! It took you {guess_count} guesses")
print("-----------------------------------------------------------")
