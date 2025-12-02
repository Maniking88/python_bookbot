def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def words_in_book(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = words_in_book(book_text)
    print(f"Found {num_words} total words")

main()