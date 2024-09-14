def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    user = input("Hi, how are you? ")
    result = convert(user)
    print(result)

main()
