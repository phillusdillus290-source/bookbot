def word_count(text):
    words = []
    word_num = 0
    words = text.split()
    word_num = len(words)
    return word_num

def char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def list_dict(dict):
    dict_list = []
    for item in dict:
        temp_dict = {}
        if len(item) == 1:
            temp_dict = {"char": item, "num": dict[item]}
            dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list