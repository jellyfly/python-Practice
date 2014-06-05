# we can use "from ex25 import *"
# then we don't have to type ex25.function any more
def break_words(stuff):
# this quoted are actually used when we type help(ex25) in python interactive GUI
# called "documentation comments"
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words.""" 
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of  the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# found an error, if there is a space before variable name, will be an IndentationError: unexpected indent. Be careful there could only be four spaces before.
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
