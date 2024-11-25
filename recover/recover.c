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
        return 1;
    }

    // Create a buffer for a block of data
    BYTE buffer[512];
    char filename[9]; // plads til "000.jpeg" + null terminator

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Dette er starten på en ny JPEG-fil
            int i = 0;
            sprintf(filename, "%03i.jpg", i);
            FILE *file = fopen(filename, "w");
            i += 1;

        }

    }
}
