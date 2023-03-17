from Sentences import get_determiner, get_noun, get_verb, get_preposition
import pytest
"""" Once I understood how to use the loop to go through the list of words it was easier to do the rest
That's why I put comments only in the first test_function
"""


def test_get_determiner():
    single_determiners = ["A", "One", "The"]
    # Repeat the statements inside
    for _ in range(4):
        # Call the funtion and define the parameters
        word = get_determiner(1)
        # Verify the word returned
        assert word in single_determiners
    plural_determiners = ["Some", "Many", "The"]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners


def test_get_noun():
    single_determiners = ["bird", "boy", "car", "cat",
                          "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_determiners
    plural_determiners = ["birds", "boys", "cars", "cats",
                          "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_determiners


def test_get_verb():
    single_present_words = ["drinks", "eats", "grows", "laughs",
                            "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, "present")
        assert word in single_present_words
    past_words = ["drank", "ate", "grew", "laughed",
                  "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1, "past")
        assert word in past_words
    present_words = ["drink", "eat", "grow", "laugh",
                     "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, "present")
        assert word in present_words
    future_words = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        word = get_verb(2, "future")
        assert word in future_words


def test_get_preposition():
    preposition_word = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from",
                        "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in preposition_word


# Call the main function
pytest.main(["-v", "--tb=line", "-rN", __file__])
