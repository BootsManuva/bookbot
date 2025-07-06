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

def character_count(book_contents):
    contents_lower_case = book_contents.lower()
    character_count_dict ={}
    for character in contents_lower_case:
        if character in character_count_dict:
            character_count_dict[character] = character_count_dict[character] + 1
        else:
            character_count_dict[character] = 1
    return character_count_dict

#ef list_dict_char(character_dict_count):
#   char_list = []
#   for item in character_dict_count:
        
def sort_on(items):
    return items["num"]

def list_char_dict(dict):
    list_dict = []
    for d in dict:
        num = dict[d]
        mini_dict = {"char": d, "num": num}
        list_dict.append(mini_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict