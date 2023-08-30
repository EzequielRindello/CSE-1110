# Import datetime
from datetime import datetime
import os
import msvcrt


def read_key():
    print("Press any key to continue...")
    msvcrt.getch()


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def compute_age(birth_str):
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(x):  # converts pounds to kilograms
    kg = x * 0.45359237
    return kg


def cm_from_in(j):  # converts centimeters to inches
    cm = j * 2.54
    return cm


def body_mass_index(x, s):  # calculates body mass index (BMI)
    bmi = x / (s ** 2) * 10000
    return bmi


# calculates basal metabolic rate
def basal_metabolic_rate(gender, weight, height, age):
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


def main():
    console_clear()
    # get the user's gender, birthdate, height, and weight.
    while True:
        try:
            gender = str(input("Please enter your gender (M or F): "))
            if gender.lower() == "f" or gender.lower() == "m":
                break
            else:
                print("Error. Please enter M(ale) or F(emale) ")
                read_key()
                console_clear()
        except:
            print("Error. Please enter a valid choice.")

    birth_str = str(input("Enter your birthdate (YYYY-MM-DD): "))
    pounds = float(input("Enter your weight in U.S. pounds: "))
    inches = float(input("Enter your height in U.S. inches: "))

    # call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions as needed.
    years = compute_age(birth_str)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    # print the results for the user to see.
    print("-------------------------------------------------------")
    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")
    print("-------------------------------------------------------")


if __name__ == "__main__":
    main()
