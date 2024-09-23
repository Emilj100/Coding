def main():
    full_version = input("Input: ")
    new_version = short(full_version)
    print(new_version)

def short(short_version):
    for c in short_version:
    print(c, end="")

main()
