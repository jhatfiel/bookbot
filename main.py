import sys
from stats import count_characters, count_words, sort_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

## create main function and call function get_book_text
def main(): 
    if (len(sys.argv) != 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    print('============ BOOKBOT ============')
    file = sys.argv[1]
    print(f'Analyzing book found at {file}...')
    book_text = get_book_text(file)
    print('----------- Word Count ----------')
    print(f'Found {count_words(book_text)} total words')
    print('--------- Character Count -------')
    characters = count_characters(book_text)
    # sort the characters by count in descending order
    characters = sort_characters(characters)
    # get the 2 most common characters that are letters 
    count = 0
    for item in characters:
        char = item['char']
        num = item['num']
        if (not char.isalpha()):
            continue
        print(f'{char}: {num}')
        count += 1
        if (count >= 2):
            break



main()