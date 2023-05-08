import math
import os
import msvcrt  # Required for Windows only


def read_key():
    print("Press any key to continue...")
    msvcrt.getch()


def err_mesagge():
    return "Error. Please enter a valid choice"


def friends_list():
    friends = []
    print("Enter a list of friends, type end when finished.")
    while True:
        try:
            answer = str(input("Please enter a friend name: "))
            if answer.lower() == "end":
                print("Your friends are: ")
                for name in friends:
                    print(name)
                read_key()
                break
            else:
                friends.append(answer)
        except:
            print(err_mesagge())


def numbers_list():
    numbers = []
    print("Enter a list of numbers, type 0 when finished.")
    while True:
        try:
            answer = float(input("Enter number: "))
            if answer == 0:
                if not numbers:
                    print("The list is empty.")
                else:
                    # Print the list
                    print("Your numbers are: ")
                    for name in numbers:
                        print(name)
                    # Sum the list
                    sum = 0
                    for number in numbers:
                        sum += number
                    print(f"The sum is: {sum}")
                    # Find and print the average
                    count = len(numbers)
                    if count == 0:
                        print("The list is empty.")
                    else:
                        average = sum / count
                        if math.isnan(average) or math.isinf(average):
                            print("The average is not valid.")
                        else:
                            print(f"The average is: {average}")
                    # Print the largest number
                    if not numbers:
                        print("The list is empty.")
                    else:
                        print("The largest number is:", max(numbers))
                    # Sort the list
                    numbers.sort()
                    print("Your list sorted: ")
                    for name in numbers:
                        print(name)
                    read_key()
                    return
            elif answer != 0:
                numbers.append(answer)
        except:
            print(err_mesagge())


def main():

    while (True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please enter a choice: ")
        try:
            user_answer = int(
                input("1: Number list\n2: Friends list\n3: Exit\n"))
            match user_answer:
                case 1:
                    numbers_list()
                case 2:
                    friends_list()
                case 3:
                    print("Goodbye!")
                    break
                case _:
                    print(err_mesagge())
        except:
            print(err_mesagge())


if __name__ == "__main__":
    main()
