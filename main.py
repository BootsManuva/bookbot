from stats import get_book_text,word_count, character_count, list_char_dict
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    count = word_count(book_text)
    word_count_message = f"Found {count} total words"
    #print(word_count_message)

    character_dict = character_count(book_text)
    char_list = list_char_dict(character_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
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
