import random
import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the user console


# return a random number to the user to guess
def random_num(): return random.randrange(0, 10)

def print_results(guess_count): return f"You guessed it right!! It took you {guess_count} guesses"


def main():
    console_clear()
    number_to_guess = random_num()
    guess_count = 0
    guess = 0
    print("Welcome to our guessing game!\nTry to guess between 0 and 10.\n")

    while number_to_guess != guess:
        try:
            guess = int(input("Enter your guess: "))
            if guess < number_to_guess:
                print("Too low!")
                guess_count = guess_count + 1
            elif guess > number_to_guess:
                print("Too high!")
                guess_count = guess_count + 1
            elif guess == number_to_guess:
                guess_count = guess_count + 1
                print(print_results(guess_count))

        except:
            print("Error. Please enter an integer.")


if __name__ == "__main__":
    main()
