friends = []
numbers = []


def friends_list():
    print("Enter a list of friends, type end when finished.")
    while True:
        answer = input("Please enter a friend name: ")
        if answer == "end":
            print("Your friends are: ")
            for name in friends:
                print(name)
            break
        else:
            friends.append(answer)


def numbers_list():
    print("Enter a list of numbers, type 0 when finished.")
    while True:
        answer = int(input("Enter number: "))
        if answer == 0:
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
            average = sum / count
            print(f"The average is: {average}")
            # Print the largest number is
            print("Largest number is:", max(numbers))
            # sorting the list
            numbers.sort()
            print("Your list sorted: ")
            for name in numbers:
                print(name)
            break
        elif answer != 0:
            numbers.append(answer)


def main():
    print("Please enter a choice: ")
    ans = input("1: Number list\n2: Friends list ")

    match ans:
        case "1":
            numbers_list()
        case "2":
            friends_list()


if __name__ == "__main__":
    main()
