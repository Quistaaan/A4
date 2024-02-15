import SpinFile

class Spinner:
    def __init__(self, text_file, synonyms):
        self.text = text_file
        self.synonyms = synonyms

    def clean_extra_lines(self):
        self.text = self.text.strip('\n')
        return self.text

    def create_synonym_dict(self):
