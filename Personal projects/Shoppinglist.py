
import math


def add_item(shopping_list, prices_list):
    """ Add an item to the shopping  list. """
    print()
    while True:
        answer = input(
            "What item would you like to add? (Please enter 0 to finish!) ")
        if answer == "0":
            break
        else:
            price = input(f"What is the price of '{answer}'?  ")
            prices_list.append(price)
            myTup = (answer, price)
            shopping_list.append(myTup)
    pass


def view_cart(shopping_list):
    """ Prints the shopping  list. """
    print("\nThe contents of the shopping cart are:")
    for x in range(len(shopping_list)):
        print(shopping_list[x][0] + " - $" + shopping_list[x][1])
    pass


def remove_item(shopping_list, prices_list):
    """ Removes an item from the shopping  list. """
    print("\nThe shopping list with indexes is:")
    for i in range(len(shopping_list)):
        item = shopping_list[i]
        print(f"{i}. {item}")

    while True:
        try:
            index = int(
                input("Which item would you like to remove?(Please enter an index!) "))
            shopping_list.pop(index)
            prices_list.pop(index)
            break
        except:
            print("Invalid index.")

    pass


def compute_total(prices_list):
    """ Computes the sum of the items from the shopping  list. """

    prices_list = list(map(float, prices_list))
    total = math.fsum(prices_list)
    print(
        f"\nThe total price of the items in the shopping cart is ${total:.2f}")
    print()
    pass


def main():
    # Creates the shopping  list.
    shopping_list = []
    # Creates a prices list to store and calculate prices.
    prices_list = []
    print("Welcome to the Shopping Cart Program!")
    while True:
        # Gets input from the user.
        print("Please select one of the following: ")
        answer = input(
            "1: Add item\n2: View cart\n3: Remove item\n4: Compute total\n5: Quit\n")
        # Based on the input from the user call the selected funtion.
        match answer:
            case "1":
                add_item(shopping_list, prices_list)
            case "2":
                view_cart(shopping_list)
            case "3":
                remove_item(shopping_list, prices_list)
            case "4":
                compute_total(prices_list)
            case "5":
                print("Thank you. Goodbye.")
                break


if __name__ == "__main__":
    main()
