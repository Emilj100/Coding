def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    grade_level = calculate_grade_level(letters, words, sentences)
    if grade_level < 1:
        print("Before Grade 1")
    elif grade_level >= 16:
        print("Grade 16+")
    else:
        print(f"Grade: {grade_level}")


def count_letters(text):
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            counter += 1
    return counter

def count_words(text):
    counter = 1
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

def calculate_grade_level(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    return round(0.0588 * L - 0.296 * S - 15.8)


main()
