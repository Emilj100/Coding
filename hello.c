#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    string player[2];
    player[0] = get_string("Player 1: ");
    player[1] = get_string("Player 2: ");

    int counter_1 = 0;
    for (int number = 0; number < 2; number += 1)
    {
        for (int i = 0, n = strlen(player[number]); i < n; i += 1)
        {
            if (player[number] == 'A' || player[number] == 'E' || player[number] == 'I' || player[number] == 'N' || player[number] == 'R'
             || player[number] == 'S' || player[number] == 'T' || player[number] == 'U')
            {
                counter_1 += 1;
            }
            else if (player[number] == 'D' || player[number] == 'G')
            {
                counter_1 += 2;
            }
            else if (player[number] == 'B' || player[number] == 'C' || player[number] == 'M' || player[number] == 'P')
            {
                counter_1 += 3;
            }
            else if (player[number] == 'F' || player[number] == 'H' || player[number] == 'V' || player[number] == 'W' || player[number] == 'Y')
            {
                counter_1 += 4;
            }
            else if (player[number] == 'K')
            {
                counter_1 += 5;
            }
            else if (player[number] == 'J' || player[number] == 'X')
            {
                counter_1 += 8;
            }
            else if (player[number] == 'Q' || player[number] == 'Z')
            {
                counter_1 += 10;
            }
        }

    }
    printf("%i\n", counter_1);

}
