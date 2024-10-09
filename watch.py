import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s, re.IGNORECASE)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
