from stats import get_total_words, get_total_chars, sorted_dict
import sys

def main():
    try:
        filepath = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    counts = sorted_dict(get_total_chars(filepath))
    
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {filepath}...\n" \
    "----------- Word Count ----------")
    print(f"Found {get_total_words(filepath)} total words")
    print("--------- Character Count -------")
    for key in counts:
        if key.isalpha():
            print(f"{key}: {counts[key]}")
main()