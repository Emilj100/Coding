#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    string player[2];
    player[0] = get_string("Player 1: ");
    player[1] = get_string("Player 2: ");

    int counter[2];
    counter[0] = 0;
    counter[1] = 0;
    for (int number = 0; number < 2; number += 1)
    {
        for (int i = 0, n = strlen(player[number]); i < n; i += 1)
        {
            if (player[number][i] == 'A' || player[number][i] == 'E' || player[number][i] == 'I' || player[number][i] == 'N' || player[number][i] == 'R'
             || player[number][i] == 'S' || player[number][i] == 'T' || player[number][i] == 'U')
            {
                counter[number] += 1;
            }
            else if (player[number][i] == 'D' || player[number][i] == 'G')
            {
                counter[number] += 2;
            }
            else if (player[number][i] == 'B' || player[number][i] == 'C' || player[number][i] == 'M' || player[number][i] == 'P')
            {
                counter[number] += 3;
            }
            else if (player[number][i] == 'F' || player[number][i] == 'H' || player[number][i] == 'V' || player[number][i] == 'W' || player[number][i] == 'Y')
            {
                counter[number] += 4;
            }
            else if (player[number][i] == 'K')
            {
                counter[number] += 5;
            }
            else if (player[number][i] == 'J' || player[number][i] == 'X')
            {
                counter[number] += 8;
            }
            else if (player[number][i] == 'Q' || player[number][i] == 'Z')
            {
                counter[number] += 10;
            }
        }

    }
    printf("%i\n", counter[0]);

}
