from stats import get_book_text,word_count, character_count, list_char_dict

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = word_count(book_text)
    word_count_message = f"Found {count} total words"
    #print(word_count_message)

    character_dict = character_count(book_text)
    char_list = list_char_dict(character_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count_message)
    print("--------- Character Count -------")
    for i in char_list:
        c = i["char"]
        n= i["num"]
        if c.isalpha() == True:
            print(f"{c}: {n}")
    print("============= END ===============")
    
main()
