from datetime import datetime
from dateutil.relativedelta import relativedelta
import random
import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_random_weights(num_items, min_weight, max_weight):
    random_weights = [round(random.uniform(min_weight, max_weight), 2)
                      for _ in range(num_items)]
    return random_weights


def sum_weights(random_weights):
    total_weight = sum(random_weights)
    return round(total_weight, 2)


def check_weight(weight, min_weight, max_weight):  # future improvement
    if weight >= min_weight and weight <= max_weight:
        return True
    else:
        return False


def create_expiration_date(current_date, years):
    current_datetime = datetime.strptime(current_date, "%Y-%m-%d %H:%M")
    expiration_date = current_datetime + relativedelta(years=years)
    return expiration_date.strftime("%Y-%m-%d %H:%M")


def main():
    min_weight = 95.0
    max_weight = 105.0
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    expiration_date = create_expiration_date(current_date, 2)
    batch_weights = generate_random_weights(10, min_weight, max_weight)
    total_weight = sum_weights(batch_weights)

    # Print results
    print("---------------------------------------------")
    print(f"Packing Date: {current_date}")
    print(f"Expiration Date: {expiration_date}")
    print("---------------------------------------------")
    print("Weight per Package:")
    # for weight in batch_weights:
    #     print(weight)
    [print(weight) for weight in batch_weights]
    print("---------------------------------------------")
    print(f"Total Weight: {total_weight} g")
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
