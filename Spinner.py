#Written By Austin Mills

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
def read_file(text_file):
    text = open(text_file)
    text = text.read()
    text = text.strip()
    text = text.lower()
    text = text.split('\n')
    text = ' '.join(text)
    return text

def make_string_list(text):
    text_list = text.split()
    return text_list

class Spinner:
    def __init__(self, text_file, synonyms):
        self.text = read_file(text_file)
        self.synonyms = create_synonym_dict(synonyms)

    def change_words(self):
        complete_changed_text = ''
        changed_text_list = []
        text_list = make_string_list(self.text)
        for word in text_list:
            random_number = random.randint(0,99)
            if word not in self.synonyms or random_number <= 50:
                changed_text_list.append(word)
            elif word in self.synonyms and random_number > 50:
                changed_text_list.append(self.synonyms[word][random.randint(0, len(self.synonyms[word]) - 1)])
        for word in changed_text_list:
            complete_changed_text = complete_changed_text + word + ' '
        return complete_changed_text
