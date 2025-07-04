def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

# could have done cleaner:
# with open(book_path) as book:
#     return book.read()

def word_count(book_contents):
    words = book_contents.split()
    return len(words)