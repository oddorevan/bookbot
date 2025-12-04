def word_counter(book_as_string):
    # splits a string into words by their whitespace
    word_list = book_as_string.split()
    num_words = len(word_list)
    return num_words


def char_counter(book_as_string):
    # counts the characters in a string and returns a
    # dictionary of how many times each character was used.
    # returns
    counts = {}
    for x in book_as_string.lower():
        counts[x] = counts.get(x, 0) + 1
    return counts
