# Import random
import random


def main():
    # Build a ramdom phrase.
    # Past the parameters for the funtions.
    first_phrase = create_phrase(quantity=1, tense="past")
    second_phrase = create_phrase(quantity=1, tense="present")
    third_phrase = create_phrase(quantity=1, tense="future")
    fourth_phrase = create_phrase(quantity=2, tense="past")
    fifth_phrase = create_phrase(quantity=2, tense="present")
    sixth_phrase = create_phrase(quantity=2, tense="future")

    # Print the ramdom phrases.
    print(first_phrase)
    print(second_phrase)
    print(third_phrase)
    print(fourth_phrase)
    print(fifth_phrase)
    print(sixth_phrase)


def get_determiner(quantity):
    # Return a randomly chosen determiner
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    word = word.capitalize()
    return word


def get_noun(quantity):
    # Return a randomly chosen moun.
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    # Return a randomly chosen verb.
    if quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif quantity != 1 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think",
                 "will run", "will sleep", "will talk", "will walk", "will write"]
    word = random.choice(words)
    return word


def get_preposition():
    # Return a randomly chosen preposition.
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from",
             "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    # Build and return a prepositional phrase
    word0 = get_preposition()
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word = word0+" "+word1.lower()+" "+word2
    return word


def create_phrase(quantity, tense):
    # I create this funtion so the main funtions result easier to read.
    # Returs a full word that is going to be stored in a variable so it can be printed in main.
    first_word = get_determiner(quantity)
    second_word = get_noun(quantity)
    third_word = get_verb(quantity, tense)
    fourth_word = get_prepositional_phrase(quantity)
    full_word = first_word+" "+second_word+" "+third_word+" " + fourth_word
    return full_word


if __name__ == "__main__":
    main()
