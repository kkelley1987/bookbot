def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    list = sort_list(count_chars(text))
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for i in range(0, len(list), 1):
        print(f"The '{list[i]['key']}' character was found {list[i]['value']} times.")
    print("--- End Report ---")

    


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(text):
    list = []

    for c in text:
        lowered = c.lower()
        found = False
        #search to see if a dictionary already exists for a letter, and if it is a letter
        for i in range (0, len(list), 1):
            if list[i]['key'] == lowered and lowered.isalpha():
                #key exists increase it's number
                list[i]['value'] += 1
                found = True
        
        if not found and lowered.isalpha():
            #dictionary doesn't exist, create it with a key of lowered and a value of 1
            new_dict = {
                'key':lowered,
                'value':1
            }
            #add to the list
            list.append(new_dict)
    return list

def sort_list(list):
    sorted_list = sorted(list, key=lambda d: d['value'], reverse=True)
    return sorted_list
            
main()