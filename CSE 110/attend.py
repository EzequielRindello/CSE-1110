import msvcrt
import os

# initialize variables
age = 0
name = ""
gender = ""
class_to_attend = ""


def read_key():
    print("Press any key to continue...")
    msvcrt.getch()


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def determine_gender():
    while True:
        gender = input("\nPlease enter your gender (M/F): ").upper()
        if gender == "F" or gender == "M":
            return gender
        else:
            print("Invalid input. Please enter 'M' for Male or 'F' for Female.")


def determine_age():
    while True:
        try:
            age = int(input("\nPlease enter your age: "))
            return age
        except:
            print("Invalid input. Please enter an integer.")


def if_men(age: int):

    if age >= 3 and age <= 10:
        class_to_attend = "Primary"
    elif age >= 11 and age <= 17:
        class_to_attend = "Young men"
    elif age >= 18:
        class_to_attend = "Elders quorum"
    else:
        class_to_attend = "The member is a baby, should go with you to your respective class"
    return class_to_attend


def if_woman(age: int):

    if age >= 3 and age <= 10:
        class_to_attend = "Primary"
    elif age >= 11 and age <= 17:
        class_to_attend = "Young women"
    elif age >= 18:
        class_to_attend = "Relief society"
    else:
        class_to_attend = "The member is a baby, should go with you to your respective class"
    return class_to_attend


def main():
    # clear the console and intruduce the user to the program
    console_clear()
    print("Welcome! This program will determine which class you should attend.\n")
    read_key()

    # get the name
    global name
    name = input("\nPlease enter your name: ").capitalize()

    # get the gender
    global gender
    gender = determine_gender()

    # get the age
    global age
    age = determine_age()

    # display the results
    console_clear()
    print("---------------------------------------------------------")
    print(f"Name: {name}\nAge: {age}\nGender: {gender}")

    global class_to_attend  # determinate the class based on the input
    if gender == "F":
        class_to_attend = if_woman(age)
        print(f"\nYou sould attend to {class_to_attend} ")
    else:
        class_to_attend = if_men(age)
        print(f"\nYou sould attend to: {class_to_attend} ")

    print("---------------------------------------------------------")


if __name__ == "__main__":
    main()
