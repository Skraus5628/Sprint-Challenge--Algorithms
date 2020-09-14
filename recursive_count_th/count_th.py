'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#To do:
    #Go through length of the "array" (word)
    #if the word contains less than 2 characters return 0, "th" is 2 characters after all!
    # check the value of "th" specifically being in the word. Return 1 for every instance of "th"


def count_th(word):
    if len(word) < 2:
        return 0

    if word[:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
