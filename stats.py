def get_book_text(filepath):  
    with open(filepath) as f:
        contents = f.read()
        return contents

def get_total_words(filepath):
    book = get_book_text(filepath)
    words = len(book.split())
    
    return words

def get_total_chars(filepath):
    book = get_book_text(filepath)
    counts = {}
    for char in book:
        if char.lower() in counts:
            counts[char.lower()] +=1
        else:
            counts[char.lower()] = 1
    return counts

def sorted_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict