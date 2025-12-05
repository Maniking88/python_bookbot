import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit[1]

book_path = sys.argv[1]

from stats import get_num_words, get_num_chars, chars_dict_to_sorted_list

def main():
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    num_chars = get_num_chars(text)

    sorted_list = chars_dict_to_sorted_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()