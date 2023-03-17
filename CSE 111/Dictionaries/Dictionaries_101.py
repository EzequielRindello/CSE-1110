# dictionaries 101

def main():

    # A dictionary is a collection of 'keys' and 'values'.
    # This is a python dictionary (note the '{}' notation).
    # Here, we have a dictionary of numbers (the 'keys'), and whether that 'key' is a prime number or not (the 'value').
    prime_numbers = {
        "1" : False,
        "2" : True,
        "3" : True,
        "4" : False,
        "5" : True,
        "6" : False,
        "7" : True,
        "8" : False,
        "9" : False,
        "10" : False
    } 

    # we can print the entire dictionary, but, like lists, this is kind of ugly, really only useful for debugging
    print(prime_numbers)

    # To get something from a dictionary, you look it up by it's key:
    # Here, prime_numbers["3"] ISN'T getting the item at index location 3. It's looking up the value in the dictionary with a 'key' of "3".
    # When it finds the item with a key of "3", it will return the value associated with that key
    is_prime = prime_numbers["3"]
    print(is_prime)

    # We can loop through a dictionary of items.
    # However, when doing this, be aware the loop variable, 'd' in this case, will only contain the 'key'.
    # So, the first time through the loop, d = "1", on the next loop, d = "2" etc. till the end of the dictionary
    for d in prime_numbers:
        print(d)

    # How can we loop through the dictionary and get *both* the key and the value?
    # Simple! Remember, we have the key (in the loop variable), and how do we get a 
    # value if we know the key? like this:
    for d in prime_numbers:
        # remember, 'd' is the key, so d = "1", then "2", then "3" etc. as we loop through the dictionary
        # to get a value from the dictionary we look up it's key:
        value = prime_numbers[d]       
        print(f"{d} = {value}")


    # ---------------------------------------------------------------------------------------------------------------
    # dictionaries are very easy to work with, and are incredibly useful!
    # dictionaries can store other types of information as well.
    #
    # For example, let's say you are writing a fantasy/adventure game.
    # One thing you have to keep track of is your player character. Dictionaries make this easy!
    # For your player, you need to keep track of certain attributes, like health, strength, speed etc.
    # You might also need to keep track of what items the player has found, like a sword, a key, a map etc.

    # let's create a player dictionary
    player = {
        "attributes" : {"health" : 100, "wisdom" : 70, "strength" : 85, "speed" : 50, "gold" : 30},
        "items" : ["sword", "key", "lantern", "map", "shield"]   
    }

    # In this dictionary, you can see that the key 'attributes' is associated with a dictionary of player attributes.
    # Let's see how we can read the amount of gold a player has:
    # First, get the value associated with the key:
    player_attributes = player["attributes"]
    # 'player_attributes' now contains a dictionary = let's look at it
    print(player_attributes)
    # Now, since player_attributes IS another dictionary, it's easy to get the amount of gold,
    # again, by looking up the value associated with the key 'gold':
    amount_gold = player_attributes["gold"]
    print(f"player has {amount_gold} gold pieces")


    # The second key in our player dictionary, 'items', is associated with a LIST of things the player has.
    # Let's look at it:
    player_items = player["items"]
    # player_items now contains a list -
    print(player_items)
    # now we can check if a player has a certain item, like this:
    if 'shield' in player_items:
        print('the player has a shield')
    else:
        print('the player has no shield')

    # Dictionaries are very powerful tools to help you organize data and get quick access to that data.
    # Make sure you really understand these concepts - you will use them a lot in your career!


if __name__ == "__main__":
    main()