#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Define constant for header size
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open input file
    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Could not open input file.\n");
        return 1;
    }

    // Open output file
    FILE *output = fopen(argv[2], "wb");
    if (output == NULL)
    {
        printf("Could not open output file.\n");
        fclose(input);
        return 1;
    }

    // Convert factor to float
    float factor = atof(argv[3]);

    // Copy header from input file to output file
    uint8_t header[HEADER_SIZE];
    if (fread(header, HEADER_SIZE, 1, input) != 1)
    {
        printf("Error reading header from input file.\n");
        fclose(input);
        fclose(output);
        return 1;
    }
    if (fwrite(header, HEADER_SIZE, 1, output) != 1)
    {
        printf("Error writing header to output file.\n");
        fclose(input);
        fclose(output);
        return 1;
    }

    // Process audio samples
    int16_t buffer;
    while (fread(&buffer, sizeof(int16_t), 1, input) == 1)
    {
        // Scale the sample
        buffer *= factor;

        // Avoid clipping
        if (buffer > 32767)
        {
            buffer = 32767;
        }
        else if (buffer < -32768)
        {
            buffer = -32768;
        }

        // Write the scaled sample to output file
        if (fwrite(&buffer, sizeof(int16_t), 1, output) != 1)
        {
            printf("Error writing sample to output file.\n");
            fclose(input);
            fclose(output);
            return 1;
        }
    }

    // Close files
    fclose(input);
    fclose(output);

    return 0;
}
