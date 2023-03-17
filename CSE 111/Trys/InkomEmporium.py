# Import the datetime class
from datetime import datetime
import csv
import math
# Keys of products_dict.
PRODUCT_INDEX = 0
VALUE_INDEX = 1
PRODUCT_PRICE_INDEX = 2
# Keys for request.
PRODUCT_REQUEST_INDEX = 0
QUANTITY_INDEX = 1
# Call the now() method to get the current date and time
current_date_and_time = datetime.now()


def read_dict(filename, key_column_index):
    # Creates an empty dictionary.
    dictionary = {}
    # Open the CSV file for reading and store a reference
    # to the opened file in a VARIABLE NAMED csv_file.
    try:
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
        return dictionary
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
    except (csv.Error, KeyError) as error:
        print(f"Error: line {reader.line_num} of {csv_file.name}"
              " is formatted incorrectly.")


def request(filename, products_dict):

    try:
        with open(filename, "rt") as csv_file:
            # Creates emty list to store values for calculations.
            quan = []
            price = []
            # create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)
            # Ignores the first line that is a header.
            next(reader)
            # Read each line of text and print the product name, requested quantity, and product price.
            for row_list in reader:
                product_code = row_list[PRODUCT_REQUEST_INDEX]
                quantity = row_list[QUANTITY_INDEX]
                product_name = products_dict[product_code][VALUE_INDEX]
                product_price = products_dict[product_code][PRODUCT_PRICE_INDEX]
                print(f"{product_name}: {quantity} @ {product_price}")
                # Append the values for the reques csv.file.
                quan.append(quantity)
                price.append(product_price)
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
    except (csv.Error, KeyError) as error:
        print(f"Error: line {reader.line_num} of {csv_file.name}"
              " is formatted incorrectly.")
    except TypeError as type_err:
        print(type_err)

    # Call the compute info funtion
    compute_info(quan, price)


def compute_info(quantity, price):

    # Does the calculations

    # Items
    quantity = list(map(float, quantity))
    total = math.fsum(quantity)
    print(f"\nNumber of Items: {total:.0f}")

    # Subtototal
    price = list(map(float, price))
    new_list = [a*b for a, b in zip(quantity, price)]
    subtotal = math.fsum(new_list)
    print(f"Subtotal: {subtotal:.2f}")

    # Sales tax
    sales_tax = 0.06
    sales_tax = subtotal*sales_tax
    print(f"Salex tax: {sales_tax:.2f}")
    total = subtotal+sales_tax
    print(f"Total: {total:.2f}")


def main():

    # Print the store name.
    print("Inkom Emporium")
    print()

    # Call the funtion to the contents of a CSV file and create the dictionary.
    products_dict = read_dict("products.csv", PRODUCT_INDEX)

    # Call the funtion passing the file and the dictionary.
    request("request.csv", products_dict)

    # Print the current date and time.
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%A %I:%M %p}")


if __name__ == "__main__":
    main()
