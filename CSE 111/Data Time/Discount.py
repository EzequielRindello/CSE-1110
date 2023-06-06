# Use the datetime library
from datetime import datetime
import os
import msvcrt


def read_key():
    print("Press any key to continue...")
    msvcrt.getch()


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    console_clear()
    current_date = datetime.now()
    day_of_week = current_date.weekday()

    # Variables rates
    disc_rate = 0.10
    tax_rate = 0.06

    # Display info and ask fot the total
    while True:
        print("This program will let you know if you have 10 % discount\n")
        try: 
            sub_total = float(input("Please enter the subtotal: "))
            break
        except:
            print("Error. Please enter a valid choice.")
            read_key()
            console_clear()

    # If statement to know the days of discount
    if sub_total >= 50 and (day_of_week == 1 or day_of_week == 2):
        discount = round(sub_total * disc_rate, 2)
        print(f"\nDiscount amount: {discount:.2f}")
        sub_total -= discount

    # Tax calculations.
    TAX = round(sub_total * tax_rate, 2)
    print(f"\nSales tax amount: {TAX:.2f}")
    total = sub_total+TAX

    # print the result.
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
