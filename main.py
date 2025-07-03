def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()

## get book text function defined. main function defined and then called
## the main funchin does not need any arguments because it provides the input for the book file itself and then prints it 
##
