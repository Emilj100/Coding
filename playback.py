def convert(text):
    text = text.replace(":)", )
    return text

def main():
    user_input = input("Hi, how are you? ")
    result = convert(user_input)
    print(result)

main()
