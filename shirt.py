import sys
import csv



user_input = sys.argv[1:]




if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

old_file = sys.argv[1].lower()
new_file = sys.argv[2].lower()

if not old_file.endswith((".jpg", "jpeg", "png")) or not new_file.endswith((".jpg", "jpeg", "png")):
    sys.exit("Invalid output")

file_name1, old_file_extension = old_file.split(".")
file_name2, new_file_extension = new_file.split(".")

if not new_file_extension == old_file_extension:
    sys.exit("Input and output have different extensions")


