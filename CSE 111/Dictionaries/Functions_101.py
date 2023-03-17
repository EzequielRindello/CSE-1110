# functions 101

# good functions
# 1. a good function should do ONE thing, and do it very well.
# 2. a good function should be short.
# 3. a good function should tell the caller what it does based on it's name.

# function that takes no parameters, and returns nothing.
# this type of function is rare - you usually you want a function
# to do something with data you pass in, or get a return value back.
def print_separator():
    print("------------------------------------------")

# function that takes 2 parameters, and returns nothing.
# add a and b, and print the sum
def  print_sum(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")

# function that takes 1 parameter and returns a value.
# can you see in the code where a value is returned?
# just like the caller of a function can pass in data in parameters,
# a function can return data to the caller through the 'return' statement.
def get_word_count(sentence):
    # split the sentence into individual words.
    # we're assuming that each word in the sentence is separated from the next word by a space.
    # each individual word will then be added to a list we call 'words'.
    words = sentence.split(" ")

    # get the number of words in the 'words' list.
    # we do this by calling another function, this one is built-in to python - len().
    # notice how len() is a function - it takes one parameter - a list, and returns the length (or count) of the items in the list.
    # note how we capture the return value from the function and store it in a variable names 'number_of_words'.
    # if we don't store it in a variable, that value will be lost and we won't be able to return the number of words in our sentence.
    number_of_words = len(words)

    # return the number of words to the caller of this function
    return number_of_words



def main():

    # -----------------------------------------------------------------------
    # call a function that takes no parameters, and returns nothing.
    # note - when calling a function, even if it takes no parameters,
    # it is still necessary to put parenthesis () after the call
    print_separator()

    # -----------------------------------------------------------------------
    # call a function that takes 2 parameters and returns nothing.
    # notice all the ways this same function can be called.
    # also notice that the function has two parameters, called 'a' and 'b'.
    # just because a function names it's parameters a certain way,
    # doesn't mean we have to pass in variables with the same name.
    # notice this first example - we're passing in variables named x and y.
    # inside the print_sum function, 'a' will get the value of 10, and 'b' will get the value of 3.
    
    # pass 10 and 3 to the function, because x = 10, and y = 3. 
    # this call should print  10 + 3 = 13
    x = 10
    y = 3
    print_sum(x,y)

    # pass 8 and 9 to the function. 
    # this call should print 8 + 9 = 17
    print_sum(8,9) 

    # this call should print 10 + 88 = 98
    val1 = 10
    print_sum(val1, 88)

    # -----------------------------------------------------------------------
    # call a function that takes 1 parameter, and returns a value.
    # the return value from the function will be the number of words in a sentence.
    # we need to store that return value in a variable in order to use it in our code.
    # if we don't store that return value in a variable, it will be lost.
    sentence1 = "the quick brown fox jumped over the lazy dog"
    # call the function, and store the return value in a variable named 'count1'
    count1 = get_word_count(sentence1)
    # now that we have stored the return value in 'count1', we can print that value
    # which should be the number of words in the sentence
    print(f"there are {count1} words in the sentence '{sentence1}'")

if __name__ == "__main__":
    main()