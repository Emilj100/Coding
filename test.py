def main():
    # Få input fra brugeren
    text = input("Text: ")

    # Beregn antallet af bogstaver, ord og sætninger
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Beregn Coleman-Liau-indekset
    index = calculate_index(letters, words, sentences)

    # Print resultatet
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    """Tæller antallet af bogstaver i teksten."""
    return sum(1 for char in text if char.isalpha())


def count_words(text):
    """Tæller antallet af ord i teksten."""
    return len(text.split())


def count_sentences(text):
    """Tæller antallet af sætninger i teksten."""
    return sum(1 for char in text if char in ".!?")


def calculate_index(letters, words, sentences):
    """Beregner Coleman-Liau-indekset."""
    L = (letters / words) * 100  # Gennemsnitligt antal bogstaver pr. 100 ord
    S = (sentences / words) * 100  # Gennemsnitligt antal sætninger pr. 100 ord
    index = round(0.0588 * L - 0.296 * S - 15.8)
    return index


if __name__ == "__main__":
    main()
