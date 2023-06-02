import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_file(filename, year_of_interest):
    """ Reads from the file """
    i = 0
    lowest = 1000
    maximun = -1
    emty_list = []
    average_min_list = []
    average_max_list = []

    # Open the file with the information.
    with open(filename) as life_file:

        # Iterate through the file one line at a time.
        for line in life_file:
            # Split up the line based on the ":"
            i = i+1
            clan_line = line.strip()
            words = clan_line.split(",")

            if i > 1:
                # Get the file and strip off any leading/trailing whitespace.
                entity = words[0]
                code = words[1]
                year = int(words[2])
                life_exp = float(words[3])

                if lowest > life_exp:
                    lowest = life_exp
                    average_min_list.append(lowest)

                if maximun < life_exp:
                    maximun = life_exp
                    average_max_list.append(maximun)

                # If the year that the user type exists in the filename appends the data to a emty list.
                if year_of_interest == year:
                    emty_list.append(life_exp)

        # Print the overal max and min from the whole file.
        a_max = max(average_max_list)
        a_min = min(average_min_list)
        print("---------------------------------------------------------------------")
        print(
            f"The overall max life expectancy is: {a_max:.2f} from Monaco in 2019")
        print(
            f"The overall min life expectancy is: {a_min:.2f} from Iceland in 1882")
        print("---------------------------------------------------------------------")

    # Creates a new list to display the data for the year of the user interest.
    # Make sure that the list is not emty to avoid errors.
    if len(emty_list) == 0:
        print(f"{year_of_interest} is not a valid year,")
        print("please select another.")
    else:
        year_of_interest_def(emty_list, year_of_interest)


def year_of_interest_def(new_list, year):

    print(f"For the year {year}: ")
    print("---------------------------------------------------------------------")
    # Convert into float whit map funtion same as a for loop.
    new_list = list(map(float, new_list))
    # Get the average.
    sum_of_list = 0
    for i in range(len(new_list)):
        sum_of_list += new_list[i]
    average = sum_of_list/len(new_list)
    print(
        f"The average life expectancy across all countries was {average:.2f}")
    # Get the max.
    max_average = max(new_list)
    print(f"The max life expectancy was {max_average:.2f}")
    # Get the min.
    min_average = min(new_list)
    print(f"The min life expectancy was {min_average:.2f}")
    print("---------------------------------------------------------------------")


def main():
    console_clear()
    # Make sure the user tipes a year in int.
    while True:
        try:
            year_of_interest = int(input("Enter the year of interest: "))
            #year_of_interest = str(year_of_interest)
            break
        except:
            print("Error. Please enter a integer")
    # Call the read_file funtion
    read_file("life.txt", year_of_interest)


if __name__ == "__main__":
    main()
