def main():
    full_version = input("Input: ")
    new_version = short(full_version)
    print(new_version)

def short(short_version):
    result = ""
    for c in short_version:
        if c not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            result += c

    return result

main()
