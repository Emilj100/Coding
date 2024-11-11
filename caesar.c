#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{

    if (argc == 2)
    {
        int key = atoi(argv[1]);
        string ciphertext = "";
        if (key > 0)
        {
            string plaintext = get_string("plaintext:  ");
            for (int i = 0, n = strlen(plaintext); i < n; i += 1)
            {
                int rotate = 0;
                if (isupper(plaintext[i]))
                {
                    rotate += ((plaintext[i] - 'A' + key) % 26) + 'A';
                }
                else if (islower(plaintext[i]))
                {
                    rotate += ((plaintext[i] - 'a' + key) % 26) + 'a';
                }
                else
                {
                    rotate += plaintext[i];
                }

                ciphertext += rotate;
            printf("%s\n", ciphertext);

            }
        }

    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure program was run with just one command-line argument

    // Make sure every character in argv[1] is a digit

    // Convert argv[1] from a `string` to an `int`

    // Prompt user for plaintext

    // For each character in the plaintext:

        // Rotate the character if it's a letter
}
