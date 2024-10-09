import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Brug et regulært udtryk til at finde iframe src, der peger på en YouTube-video
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s, re.IGNORECASE)

    # Hvis vi fandt et match, opbyg den korte URL, ellers returner None
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
