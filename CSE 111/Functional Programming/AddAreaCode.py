def main():
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        phone_numbers = read_list("phone_numbers.txt")

        # Print the list of phone numbers which will show that
        # some of the phone number don't have an area code.
        print(phone_numbers)

        # Some of the phone numbers in phone_numbers.txt do not start
        # with an area code. Replace each short phone number with a
        # phone number that begins with the area code "208-" To do this,
        # call the map function and pass the add_area_code function and
        # the list of phone numbers as arguments to the map function.
        new_numbers = list(map(add_area_code, phone_numbers))

        # Print the list with the corrected phone numbers.
        print(new_numbers)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def add_area_code(phone_number):
    if len(phone_number) < 12:
        phone_number = "208-" + phone_number
    return phone_number


def read_list(filename):
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


if __name__ == "__main__":
    main()
