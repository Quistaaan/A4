import SpinFile

import random
def create_synonym_dict(synonymfile):
    text_list = []
    with open(synonymfile) as file:
        for line in file:
            text_list.append(line.strip())
    response_dict = {}
    for line in text_list:
        key_and_value = line.split(':')
        response_dict[key_and_value[0]] = (key_and_value[1])
    for key in response_dict:
        response_dict[key] = response_dict[key].split(',')
    return response_dict

def clean_extra_lines(text):
    text = text.strip('\n')
    return text

def make_string_list(text):
    text_list = text.split()
    return text_list

class Spinner:
    def __init__(self, text_file, synonyms):
        self.text = clean_extra_lines(text_file)
        self.synonyms = create_synonym_dict(synonyms)

    def change_words(self):
        changed_text_list = []
        text_list = make_string_list(self.text)
        for word in text_list:
            if word not in self.synonyms:
                changed_text_list.append(word)
            if word in self.synonyms:
                changed_text_list.append(self.synonyms[word][random.randint(0, len(self.synonyms[word]) - 1)])
        return changed_text_list
