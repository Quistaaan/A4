#Written By Austin Mills
#https://github.com/Quistaaan/A4

import Spinner

def main():
    spinner = Spinner.Spinner('essay.txt', 'synonyms-simplified.txt')
    print('original: ' + spinner.text + '\n')
    print('changed: ' + spinner.change_words())
    print(spinner.change_words())
    print(spinner.change_words())
if __name__ == "__main__":
    main()