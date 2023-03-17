# Import ramdom and creates a list of numbers.
import random


def main():
    numbers = [11.4, 23.4, 16.7]
    print(f"numbers {numbers}")
    # Add one random numbers to the numbers list.
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    # Add three random numbers to the numbers list.
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")
    # Creates an empty list of words
    words = []
    # Appends words to the list and print the result.
    append_random_words(words, 5)
    print(f"words {words}")


def append_random_numbers(numbers, quantity=1):
    """Append a random number into the numbers list.
    The random number is between 0 and 100."""
    # Randomly choose quantity of numbers and append to the numbers list.
    for i in range(quantity):
        num = random.uniform(0, 100)
        roundnum = round(num, 1)
        numbers.append(roundnum)


def append_random_words(words, quantity=1):
    """Append quantity randomly chosen words onto the words list."""
    # list of words to randomly choose from.
    random_words = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]
    # Randomly choose quantity words and append them onto random_words.
    for _ in range(quantity):
        word = random.choice(random_words)
        words.append(word)


if __name__ == "__main__":
    main()
