def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.split()
    word_count = len(words) 
    characters_dict = count_charaters(file_contents)
    print_report(book_path, word_count, characters_dict)

def sort_on(dict):
    return dict["count"]

def count_charaters(book):
    characters_dict = {}
    for character in book:
        character = character.lower()
        if character not in characters_dict:
            characters_dict[character] = 1
        else:
            characters_dict[character] += 1
    return characters_dict

def print_report(book_path, num_words, characters_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n \n")
    character_count_list = []
    for key in characters_dict:
        character_count_list.append({"name": key, "count": characters_dict[key]})
    character_count_list.sort(reverse=True, key=sort_on)

    for character in character_count_list:
        if character["name"].isalpha():
            print(f"The '{character["name"]}' character was found {character["count"]} times")
    print("--- End report ---")
main()