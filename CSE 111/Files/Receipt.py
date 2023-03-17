import csv
# Keys of products_dict.
PRODUCT_INDEX = 0
VALUE_INDEX = 1
# Keys for request.
PRODUCT_REQUEST_INDEX = 0
QUANTITY_INDEX = 1


def read_dict(filename, key_column_index):
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
    return dictionary


def request(filename, products_dict):

    with open(filename, "rt") as csv_file:
        # create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # Ignores the first line that is a header.
        next(reader)
        # Read each line of text and print the product name, requested quantity, and product price.
        for row_list in reader:
            PRODUCT_PRICE_INDEX = 2
            product_code = row_list[PRODUCT_REQUEST_INDEX]
            quantity = row_list[QUANTITY_INDEX]
            product_name = products_dict[product_code][VALUE_INDEX]
            product_price = products_dict[product_code][PRODUCT_PRICE_INDEX]
            print(f"{product_name}: {quantity} @ {product_price}")


def main():
    # Call the funtion to the contents of a CSV file and create the dictionary.
    products_dict = read_dict("products.csv", PRODUCT_INDEX)
    # Print the dictionary.
    print("All Products")
    print(products_dict)
    # Call the funtion passing the file and the dictionary.
    print()
    print("Requested Items")
    request("request.csv", products_dict)


if __name__ == "__main__":
    main()
