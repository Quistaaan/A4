#Written By Austin Mills

import Spinner

def main():
    spinner = Spinner.Spinner('essay.txt', 'synonyms-simplified.txt')
    print('original: ' + spinner.text + '\n')
    print('changed: ' + spinner.change_words())
if __name__ == "__main__":
    main()