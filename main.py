from stats import get_book_text, word_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = word_count(book_text)
    word_count_message = f"{count} words found in the document"
    print(word_count_message)

main()


