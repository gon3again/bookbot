import sys
from stats import get_number_of_words
from stats import get_number_of_characters
from stats import get_report_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(str(path))
    num_words = get_number_of_words(text)
    num_characters = get_number_of_characters(text)
    report_list = get_report_list(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in report_list:
        print(f"{dict["char"]}: {dict["num"]}")


main()