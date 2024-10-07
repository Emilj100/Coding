import sys
import os
from PIL import Image, ImageOps

def main():
    # Tjekker for korrekte kommandolinjeargumenter
    check_arguments()

    old_file = sys.argv[1]
    new_file = sys.argv[2]

    try:
        # Åbner inputbilledet og t-shirten
        input_image = Image.open(old_file)
        shirt_image = Image.open("shirt.png")

        # Tilpasser inputbilledet til t-shirtens størrelse
        input_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlejrer t-shirten på inputbilledet med korrekt maske for gennemsigtighed
        input_image.paste(shirt_image, (0, 0), shirt_image)

        # Gemmer det nye billede med det rigtige output filnavn
        input_image.save(new_file)
    except FileNotFoundError:
        sys.exit("Input file does not exist")

def check_arguments():
    # Sikrer at der er præcis to kommandolinjeargumenter
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    old_file = sys.argv[1]
    new_file = sys.argv[2]

    # Brug af os.path.splitext til at finde filtypen på en sikker måde
    _, old_file_ext = os.path.splitext(old_file.lower())
    _, new_file_ext = os.path.splitext(new_file.lower())

    # Tjekker for gyldige filtyper og om filendelserne matcher
    valid_extensions = (".jpg", ".jpeg", ".png")
    if old_file_ext not in valid_extensions or new_file_ext not in valid_extensions:
        sys.exit("Invalid file extension")

    if old_file_ext != new_file_ext:
        sys.exit("Input and output file extensions do not match")

if __name__ == "__main__":
    main()

