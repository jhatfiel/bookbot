def count_words(text):
    return len(text.split())

def count_characters(text):
    # return an object with properties that are each character and their counts
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_num(item):
    return item['num']

def sort_characters(char_count):
    # convert to list of char/num pairs
    list = []
    for char, num in char_count.items():
        list.append({'char': char, 'num': num})
    list.sort(key=get_num, reverse=True)
    return list