import SpinFile

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
class Spinner:
    def __init__(self, text_file, synonyms):
        self.text = text_file
        self.synonyms = create_synonym_dict(synonyms)

    def clean_extra_lines(self):
        self.text = self.text.strip('\n')
        return self.text