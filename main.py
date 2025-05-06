import sys
from stats import count_words
from stats import count_characters
from stats import print_report


def get_book_text(path):
    with open(path) as f:
        newfile = f.read()
        wordcount = count_words(newfile)
        new_list = count_characters(newfile)
        print_report(new_list, wordcount, sys.argv[1])


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(sys.argv[1])

main()

