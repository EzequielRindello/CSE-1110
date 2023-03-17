# Import modules
import random
from datetime import datetime
# Get the current date and time from datatime.
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%A %I:%M %p}")
# List of options.
options = ["paper", "rock", "scissors"]


def prints(y, m): print(f"You: {y} Mike: {m}")  # Prints results.


def main():
    print("You will play against Mike!")
    while True:
        answer = input("Selec your choice: ")
        answer = answer.lower()
        result = random.choice(options)

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
