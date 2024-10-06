import sys
import csv



user_input = sys.argv[1:]




if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

old_file = sys.argv[1].lower()
new_file = sys.argv[2].lower()

if not old_file.endswith(".jpg" or "jpeg" or "png") and new_file.endswith(".jpg" or "jpeg" or "png"):
    sys.exit("Invalid output")




