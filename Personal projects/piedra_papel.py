# Import modules
import random
import os
# List of options.
OPTIONS = ["paper", "rock", "scissors"]


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def prints(you, mike): print(f"You: {you} \nMike: {mike}")  # Prints results.


def main():
    console_clear()
    print("Welcome to our Rock-Paper-Scissors Game! ")
    print("\nYou will play against Mike!")
    while True:
        answer = input("\nSelec your choice(paper, rock, scissors): ")
        answer = answer.lower()
        result = random.choice(OPTIONS)

        if answer == result:
            prints(answer, result)
            print("tie!")
        elif answer == "paper" and result == "rock":
            prints(answer, result)
            print("You win :)")
            break
        elif answer == "paper" and result == "scissors":
            prints(answer, result)
            print("You loose :(")
            break
        elif answer == "rock" and result == "scissors":
            prints(answer, result)
            print("You win :)")
            break
        elif answer == "rock" and result == "paper":
            prints(answer, result)
            print("You loose :(")
            break
        elif answer == "scissors" and result == "paper":
            prints(answer, result)
            print("You win :)")
            break
        elif answer == "scissors" and result == "rock":
            prints(answer, result)
            print("You loose :(")
            break
        else:
            print("Error. Please enter a valid choice.")


if __name__ == "__main__":
    main()
