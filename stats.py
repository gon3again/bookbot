def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_characters(text):
    characters = {}
    for char in text:
        if char.lower() not in characters:
            characters[char.lower()] = 0
        characters[char.lower()] += 1
    return characters

def sort_on(items):
    return items["num"]

def get_report_list(dict):
    dict_list = []
    for key in dict :
        # print(f"key: {key} val: {dict[key]}")
        dict_list.append({"char": key, "num": dict[key]})

    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
    

