def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentence = count_sentences(text)

    calculate_grade_level(letters, words, sentence)


def count_letters(text):
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            counter += 1
    return counter

def count_words(text):
    counter = 0
    for i in range(len(text)):
        if text[i].isspace():
            counter += 1
    return counter

def count_sentences(text):
    counter = 0
    for i in range(len(text)):
        if text[i] == "?" or text[i] == "." or text[i] == "!":
            counter += 1
        return counter

def calculate_grade_level(letters, words, sentence):
    


main()
