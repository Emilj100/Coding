def main():
    text = input("Text: ")

    count_letters(text)


def count_letters(text):
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            counter += 1
    print(counter)


main()
