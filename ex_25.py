def break_words(stuff):
    """this funciton will beak up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_words(words):
    """print the first words after popping it."""
    word = words.pop(0)
    print(word)

def print_last_words(words):
    """prints the last words after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """take in  a full sent. and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the 1st and last words in a sentence"""
    word = break_words(sentence)
    print_first_words(word)
    print_last_words(word)

def print_first_last_sorted(sentence):
    """sort the sentence and print the first and last one."""
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)
