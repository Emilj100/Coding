def main():
    full_version = input("Input: ")
    new_version = short(full_version)
    print("Output: ", new_version)

def short(short_version):
    result = ""
    for c in short_version:
        if c == ["a", "e", "i", "o", "A", "E", "I", "O", "U"]:
            result -= c
        else:
            result += c

    return result

main()
