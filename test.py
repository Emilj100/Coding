import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Brug et regulært udtryk til at finde alle forekomster af "um" som et helt ord, case-insensitivt
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
