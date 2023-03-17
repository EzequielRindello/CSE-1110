
"""
@author Ezequiel Rindello

"""

# Import modules.
import math
from datetime import datetime
# Get the current date and time from datatime.
current_date_and_time = datetime.now()


def menu():
    print("Please select one of the following: ")
    print("----------------------------------------------")
    print("1: Calculate areas")
    print("2: Convert units")
    print("3: Quit")
    print("----------------------------------------------")
    answer = input()
    return answer

def prints(x):  # Display results with two decimals.
    print("----------------------------------")
    print(f"The result is: {x:.2f}")
    print("----------------------------------")


# Compute the area of a circle.
def area_of_a_circle(radio): return math.pi*(radio**2)


# Compute the area of a rectangle.
def area_of_a_rectangle(width, height): return width * height


def area_of_a_square(side): return side*side  # Compute the area of a square.


# Convert celcius to fahr.
def cels_to_fahr(cels): return (cels * 9/5) + 32


def fahr_to_cels(fahr): return (fahr - 32) * 5/9  # Convert fahr to celcius.


def kg_to_lb(kg): return (kg * 2.205)  # Convert kilograms to pounds.


def lb_to_kb(lb): return (lb // 2.205)  # Convert pounds to kilograms.


def main():  # Main funtion.

    print("Welcome to the Advanced calculator program!")
    # Loop for the menu of the program so the user can use it multiple times if she/he wants.
    while True:
        # Gets input from the user.
        answer =menu()

        # Based on the input from the user call the selected funtion.
        match answer:
            case "1":
                while True:
                    area = input(
                        "Select one\n1: Square\n2: Circle\n3: Rectangle\n")
                    if area == "1":
                        try:
                            side = float(input("Enter the side: "))
                            result = area_of_a_square(side)
                            prints(result)
                            break
                        except:
                            print("Error. Please enter a valid number.")

                    elif area == "2":
                        try:
                            radio = float(input("Enter the radio: "))
                            result = area_of_a_circle(radio)
                            prints(result)
                            break
                        except:
                            print("Error. Please enter a valid number.")

                    elif area == "3":
                        try:
                            width = float(input("Enter the width: "))
                            height = float(input("Enter the height: "))
                            result = area_of_a_rectangle(width, height)
                            prints(result)
                            break
                        except:
                            print("Error. Please enter a valid number.")
                    else:
                        print("Error. Please enter a valid choice.")
            case "2":
                while True:
                    area = input("Select one:\n1: Weight\n2: Temperatures\n")
                    if area == "1":
                        while True:
                            try:
                                weight = float(input("What is your weight? "))
                                unit = str(input("In (kg) or (lb)? "))
                                if unit.lower() == "kg":
                                    conversion = kg_to_lb(weight)
                                    prints(conversion)
                                    break
                                elif unit.lower() == "lb":
                                    conversion = lb_to_kb(weight)
                                    prints(conversion)
                                    break
                            except ValueError:
                                print("Error. Please enter a valid number.")
                    elif area == "2":
                        while True:
                            try:
                                temperature = float(
                                    input("What is your temperature? "))
                                unit = str(input("In (C) or (F)? "))
                                if unit.lower() == "c":
                                    conversion = cels_to_fahr(temperature)
                                    prints(conversion)
                                    break
                                elif unit.lower() == "f":
                                    conversion = fahr_to_cels(temperature)
                                    prints(conversion)
                                    break
                            except ValueError:
                                print("Error. Please enter a valid number.")
                    break
            case "3":
                print(f"{current_date_and_time:%A %I:%M %p}")
                print("\nThank you for using our program, goodbye!")
                break
            case _:
                print("Invalid input.")



# Call the main funtion.
# If this file is simply
# imported, then skip the call to main.
if __name__ == "__main__":
    main()
