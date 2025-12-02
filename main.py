def main(book_as_path):
    book_contents = get_book_text(book_as_path)
    num_words = word_counter(book_contents)
    return print(f"Found {num_words} total words")


def get_book_text(book_path):
    # reads the text of a book from the given file path, returns the text as a string
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents


def word_counter(book_as_string):
    # splits a string into words by their whitespace
    word_list = book_as_string.split()
    num_words = len(word_list)
    return num_words


main("books/frankenstein.txt")
