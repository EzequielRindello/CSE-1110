# Use the datetime library
from datetime import datetime


def main():
    current_date = datetime.now()
    day_of_week = current_date.weekday()

    # Variables rates
    disc_rate = 0.10
    tax_rate = 0.06

    # Display info
    print("This program will let you know if you have 10 % discount")
    sub_total = float(input("Please enter the subtotal: "))

    # If statement to know the days of discount
    if sub_total >= 50 and (day_of_week == 1 or day_of_week == 2):
        discount = round(sub_total * disc_rate, 2)
        print(f"Discount amount: {discount:.2f}")
        sub_total -= discount

    # Tax calculations.
    TAX = round(sub_total * tax_rate, 2)
    print(f"Sales tax amount: {TAX:.2f}")
    total = sub_total+TAX

    # print the result.
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
