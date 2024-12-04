def main():
    text = input("Text: ")

    letters = count_letters(text)
    


def count_letters(text):
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            counter += 1
    return counter


main()
