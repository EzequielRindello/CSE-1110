import os
import msvcrt  # Required for Windows only


def main():
    console_clear()
    print("This program computes the fuel efficiency of your vehicle in miles per gallon.\n")

    while True:
        try:
            # Get an odometer value in U.S. miles from the user.
            start_miles = float(
                input("Enter the first odometer reading (miles): "))
            # Get another odometer value in U.S. miles from the user.
            end_miles = float(
                input("Enter the second odometer reading (miles): "))
            # Get a fuel amount in U.S. gallons from the user.
            amount_gallons = float(
                input("Enter the amount of fuel used (gallons): "))
            break
        except:
            print("Error. Please enter a valid choice!")
            read_key()
            console_clear()

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    lp100k = lp100k_from_mpg(mpg)

    print(f"\nThe fuel efficiency is {mpg:.1f} miles per gallon")
    print(f"and {lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles: float, end_miles: float, amount_gallons: float):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel."""
    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg: float):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value."""
    lp100k = 235.215 / mpg
    return lp100k


def read_key():
    print("Press any key to continue...")
    msvcrt.getch()


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
