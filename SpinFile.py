import Spinner
def read_file(text_file):
    text = text_file.read()
    text = text.strip()
    text = text.lower()
    return text
def main():
    original_text = read_file(open ('essay.txt'))
    print('Original: ' + original_text)
    spinner = Spinner.Spinner(original_text, 'synonyms-simplified.txt')
    print(spinner.clean_extra_lines())
    print(spinner.synonyms)


if __name__ == "__main__":
    main()