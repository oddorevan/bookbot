def word_counter(book_as_string):
    # splits a string into words by their whitespace
    word_list = book_as_string.split()
    num_words = len(word_list)
    return num_words
