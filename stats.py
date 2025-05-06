def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def count_words(path_to_book):
    str = get_book_text(path_to_book)
    list_of_words = str.split()
    return len(list_of_words)

def num_times_each_char(text_from_book):
    char_dict = dict()
    for i in text_from_book:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_char_dict(char_dict):
    raw_list = list()
    for k in char_dict:
        raw_list.append({"char":k,"num":char_dict[k]})
    
    raw_list.sort(reverse=True,key=lambda x: x["num"])
    return raw_list

