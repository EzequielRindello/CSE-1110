# Funtion that gets intital
def get_initial(name):
    initial = name[0:1].upper()
    return initial

# Ask the user for their names
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# Call the funtion and printed
print("Your initials are: "
      + get_initial(first_name)
      + get_initial(last_name))
