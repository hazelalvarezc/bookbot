def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unique_carachters = count_letters(text)
    print(f"-- Report on {book_path} --")
    print(f"{num_words} words found in the document")
    print()
    char_list(unique_carachters)
    print("-- End of report --")
   
    #print("this is characters:", characters)
    

    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    letter_dict = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i in letter_dict:
            letter_dict[i] += 1
        elif i not in letter_dict:
            letter_dict[i] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def char_list(dict): 
    list_char_dict = []
    for key in dict:
        if key.isalpha() == True:
            char_dict = {}
            char_dict["char"] = key
            char_dict["num"] = dict[key]
            list_char_dict.append(char_dict)
            list_char_dict.sort(reverse=True, key=sort_on)
    for item in list_char_dict:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    






    









main()
