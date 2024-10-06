import sys
from PIL import Image, ImageOps



user_input = sys.argv[1:]
old_file = sys.argv[1].lower()
new_file = sys.argv[2].lower()
file_name1, old_file_extension = old_file.split(".")
file_name2, new_file_extension = new_file.split(".")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif not old_file.endswith((".jpg", "jpeg", "png")) or not new_file.endswith((".jpg", "jpeg", "png")):
    sys.exit("Invalid output")

elif not new_file_extension == old_file_extension:
    sys.exit("Input and output have different extensions")



background_image = Image.open(old_file)
overlay_image = Image.open(new_file)


overlay_image = ImageOps.fit(overlay_image, background_image.size)


background_image.paste(overlay_image, (0, 0), overlay_image)


background_image.save(new_file)
