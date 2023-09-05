import os
import msvcrt  # Required for Windows only

NAMES = []
BALANCES = []  # create global emty lists


def read_key():
    print("Press any key to continue...")
    msvcrt.getch()


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def err_mesagge():
    return "Error. Please enter a valid choice"


def menu():
    return int(input("1: Create accounts\n2: Accounts info\n3: Uptate Acount\n4: Exit\n"))


def create_account():
    name = ""
    print("\nEnter the names and balances of bank accounts (type: quit when done)")
    # build the lists
    while name != "quit":
        name = input("What is the name of this new account? ")

        if name != "quit":
            try:
                balance = float(input(f"What is the balance of {name}? "))
                NAMES.append(name)
                BALANCES.append(balance)
            except:
                print(err_mesagge())
                read_key()


def accounts_info():
    # display all of the accounts with their balances
    # compute the total at the same time.
    total = 0
    if len(NAMES) == 0 & len(BALANCES) == 0:
        print("The list is empty")
    else:
        print("\nAccount Information:\n")
        print(
            "------------------------------------------------------------------------------")
        for i in range(len(NAMES)):
            print(f"{i}. {NAMES[i]} - ${BALANCES[i]:.2f}")

            total += BALANCES[i]

        average = total / len(BALANCES)

        print(f"\nTotal: ${total:.2f}")
        print(f"Average: ${average:.2f}")

        # Stretch Challenges:

        # Find the highest balance:
        highest_name = None
        highest_balance = -1

        for i in range(len(NAMES)):
            name = NAMES[i]
            balance = BALANCES[i]

            if balance > highest_balance:
                # We have a new highest!
                highest_balance = balance
                highest_name = name

        print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")
        print(
            "------------------------------------------------------------------------------")


def update_acount():
    for i in range(len(NAMES)):
        print(f"{i}. {NAMES[i]} - ${BALANCES[i]:.2f}")
    try:
        index = int(input("What account index do you want to update? "))
        new_amount = float(
            input(f"What is the new amount of {NAMES[index]}? "))
        BALANCES[index] = new_amount
    except:
        console_clear()
        print(err_mesagge())
        read_key()


def main():
    console_clear()
    print("Welcome to our program! Please choose one of the following options.")

    while True:
        try:
            answer = menu()
            match answer:
                case 1:
                    create_account()
                    console_clear()
                case 2:
                    console_clear()
                    accounts_info()
                    read_key()
                    console_clear()
                case 3:
                    update_acount()
                    console_clear()
                case 4:
                    console_clear()
                    print("Goodbye!")
                    break
                case _:
                    print(err_mesagge())
        except:
            print(err_mesagge())


if __name__ == "__main__":
    main()
