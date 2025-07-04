def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def word_count(book_contents):
    words = book_contents.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = word_count(book_text)
    word_count_message = f"{count} words found in the document"
    print(word_count_message)

main()


