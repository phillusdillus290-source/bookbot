import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

from stats import char_count, word_count, list_dict

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    words_counted = word_count(text)
    print(f"Found {words_counted} total words")
    print("--------- Character Count -------")
    char_counted = char_count(text)
    char_counted_list = list_dict(char_counted)
    for char in char_counted_list:
        print(f"{char["char"]}: {char["num"]}")

main()