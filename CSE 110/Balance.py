print("Enter the names and balances of bank accounts (type: quit when done)")

# create emty lists
NAMES = []
BALANCES = []

name = None

# build the lists
while name != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        balance = float(input("What is the balance? "))

        NAMES.append(name)
        BALANCES.append(balance)

# display all of the accounts with their balances
# compute the total at the same time.
total = 0

print("\nAccount Information:")
for i in range(len(NAMES)):
    print(f"{i}. {NAMES[i]} - ${BALANCES[i]:.2f}")

    total += BALANCES[i]

average = total / len(BALANCES)

print()
print(f"Total: ${total:.2f}")
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

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        BALANCES[index] = new_amount

    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(NAMES)):
        print(f"{i}. {NAMES[i]} - ${BALANCES[i]:.2f}")
