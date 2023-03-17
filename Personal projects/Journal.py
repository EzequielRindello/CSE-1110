"""
@author Ezequiel Rindello

"""

import random
from datetime import datetime
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%A %I:%M %p}")

Journal = []


def main():  # Main funtion
    while True:

        menu()
        Answer = input()

        match Answer:
            case "1":
                Journal = write()
            case "2":
                print(Journal)
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Error. Please select one of the following.")


def menu():  # Display the menu
    print("What would you like to do? ")
    print("1.Write")
    print("2.Display")
    print("3.Load")
    print("4.Save")
    print("5.Quit")


def write():
    Journal = []
    promps = ["What brings you joy? ", "Describe a place where you felt happiest. ",
              "What is something that you would like to change about yourself? How can you change it? ",
              "If you are granted a wish, what would you wish for and why? ",
              "How could you make someone you care about feel better if he/she just lost something important to them? "]
    promp = random.choice(promps)
    answer = input(promp)
    Journal.append(answer)
    return Journal


main()
