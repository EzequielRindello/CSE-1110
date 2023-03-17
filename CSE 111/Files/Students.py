import csv


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary."""
    # Creates an empty dictionary.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a VARIABLE NAMED csv_file.
    with open(filename, "rt") as csv_file:
        # create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # Ignores the first line that is a header.
        next(reader)
        # Read each line of text and convert it into a list for the counpoud dictionary.
        for row_list in reader:
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]
            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


def main():
    # The column headings and indexes.
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    # Call the funtion to the contents of a CSV file and create the dictionary.
    students_dict = read_dict("students.csv", I_NUMBER_INDEX)
    # Get an I-Number from the user.
    # Get an I-Number from the user.
    inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")

    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    inumber = inumber.replace("-", "")

    # Determine if the user input is formatted correctly.
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if inumber not in students_dict:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = students_dict[inumber]
                name = value[NAME_INDEX]

                # Print the student name.
                print(name)


if __name__ == "__main__":
    main()
