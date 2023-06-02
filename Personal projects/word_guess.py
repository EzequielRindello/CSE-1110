import random

def convert_string(word, count):
    # Creates a new wor for the hint.
    new_word = word
    for i in range(0, len(word)):
        if ord(word[i]) != 32:
            new_word = new_word.replace(word[i], '_ ')
    print(f"Your word has {count} letters")
    print(f"Your hint is: {new_word}")

def intro():# Intro
    print("Welcome to the word guessing game!")
    print("You have 10 attempts to guess the word")
    print("Guess the brand of the car!")

# Main loop
def main():
    keep_playing = "yes"
    secret_word = ""
    intro()
    while keep_playing == "yes":
        # Creates a list and pass a value to a variable.
        guess_count = 0
        words = ["Honda", "Audi", "Fiat", "Tesla", "Toyota"]

        # Creates the word and count the length.
        secret_word = random.choice(words)
        word_count = len(secret_word)

        # Call the funtion for the hint.
        convert_string(secret_word, word_count)

        # Guess loop.
        while True:
            answer = input("Enter tour guess: ")
            answer = answer.capitalize()
            if answer != secret_word:
                for char in secret_word:
                    if char in answer:
                        print(char)
                    else:
                        print("_")
                guess_count = guess_count + 1
                if guess_count == 10:
                    print("You already used your ten attempts,you lost. :(")
                    break
            elif answer == secret_word:
                print("\nCongratulations! You guessed it!")
                print(f"It took you {guess_count} guesses :)")
                break

        # Loop for reapeat the game.
        while True:
            answer = input(
                "Would you like to play again? Please enter Yes or No : ")
            if answer.lower() == "yes":
                break
            elif answer.lower() == "no":
                print("Goodbye!")
                keep_playing = "no"
                break
            else:
                print("Error.Please enter Yes or No")

# Call the main funtion.
if __name__ == "__main__":
    main()
