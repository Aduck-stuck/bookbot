from sys import argv

if len(argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    import sys
    sys.exit(1)

book_path = argv[1]

from stats import get_book_text
from stats import text_count_characters
from stats import get_num_words
from stats import sort_textcount

text = get_book_text(book_path)
total = text.split()

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    get_num_words(book_path)
    print("--------- Character Count -------")
    sort_textcount(book_path)
    print("============= END ===============")


if __name__ == "__main__":
    main()

