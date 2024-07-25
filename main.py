def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_text = get_num_text(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def chars_dict_to_sorted_list(num_chars_dict):
    def sort_on(dict_item):
        return dict_item["num"]

    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

    
def get_num_text(text):
    letters = {}
    for l in text:
        lowered_text = l.lower()
        if lowered_text in letters:
            letters[lowered_text] += 1
        else:
            letters[lowered_text] = 1
    return letters



main()