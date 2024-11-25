#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer for a block of data
    BYTE buffer[512];
    char filename[9]; // plads til "000.jpeg" + null terminator
    FILE *currentfile = NULL; // Pointer til den åbne JPEG-fil
    int fileIndex = 0;        // Tæller for JPEG-filer

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Check if this block is the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If a file is already open, close it
            if (currentfile != NULL)
            {
                fclose(currentfile);
            }

            // Create a new file
            sprintf(filename, "%03i.jpg", fileIndex);
            currentfile = fopen(filename, "w");
            if (currentfile == NULL)
            {
                printf("Could not create file %s.\n", filename);
                return 1;
            }
            fileIndex++;
        }

        // Write to the currently open file, if any
        if (currentfile != NULL)
        {
            fwrite(buffer, 1, 512, currentfile);
        }
    }

    // Close any remaining open file
    if (currentfile != NULL)
    {
        fclose(currentfile);
    }

    // Close the memory card file
    fclose(card);

    return 0;
}
