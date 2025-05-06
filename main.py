from stats import count_words,num_times_each_char,get_book_text,sort_char_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]

    num_words = count_words(path_to_book)
    print(f"{num_words} words found in the document")
    book_contents = get_book_text(path_to_book).lower()
    char_dict = num_times_each_char(book_contents)
    sorted_data = sort_char_dict(char_dict)
    print_report(path_to_book,num_words,sorted_data)

def print_report(path_to_book,num_words,sorted_data):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_data:
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")


main()