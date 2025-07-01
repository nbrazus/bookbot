def get_book_text(filepath):  
    with open(filepath) as f:
        contents = f.read()
        return contents

def get_total_words():
    book = get_book_text("books/frankenstein.txt")
    words = len(book.split())
    
    return words

def get_total_chars():
    book = get_book_text("books/frankenstein.txt")
    counts = {}
    for char in book:
        if char.lower() in counts:
            counts[char.lower()] +=1
        else:
            counts[char.lower()] = 1
    return counts