import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the user console


def cels_from_fahr(fahr):
    return (fahr * 9/5) + 32  # convert celcius to fahr.


def windchill(temperature):
    for x in range(0, 60, 5):
        x += 5
        Wind_Chill = 35.74 + (0.6215*temperature) - \
            (35.75 * (x**0.16)) + (0.4275*temperature*(x**0.16))
        print(
            f"At temperature {temperature:.2f}F, and wind speed at {x} mph. The windchill is: {Wind_Chill:.2f}F. ")


def main():
    console_clear()
    
    while True:
        try:
            temperature = float(input("What is the temperature? "))
            break
        except:
            print("Error. Please enter a valid number!")

    while True:
        unit = input("Fahrenheit or Celsius (F/C)? ")
        unit = unit.upper()
        if unit == "F":
            print()
            windchill(temperature)
            print()
            break
        elif unit == "C":
            print()
            converted_temperature = cels_from_fahr(temperature)
            windchill(converted_temperature)
            print()
            break
        else:
            print("Error. Please enter F or C.")


if __name__ == "__main__":
    main()
