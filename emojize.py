emoji_dict = {
    ":thumbsup:": "👍",
    ":thumbs_up:": "👍",
    ":grinning:": "😀",
    ":smile:": "😄",
    ":heart:": "❤️",
    ":sun:": "☀️"
    # Tilføj flere emojis og deres aliaser efter behov
}

# Få input fra brugeren
user_input = input("Input: ")

# Gå igennem hver nøgle i ordbogen og erstat aliaser med den tilsvarende emoji
for code, emj in emoji_dict.items():
    user_input = user_input.replace(code, emj)

# Udskriv resultatet med de erstattede emojis
print(f"Output: {user_input}")
