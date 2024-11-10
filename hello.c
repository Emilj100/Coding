#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    
    string player[0] = get_string("Player 1: ");
    string player[1] = get_string("Player 2: ");

    int counter_1 = 0;
    for (int number = 0; number < 2; number += 1)
    {
        for (int i = 0, n = strlen(player_1); i < n; i += 1)
        {
            if (player_1[number] == 'A' || player_1[number] == 'E' || player_1[number] == 'I' || player_1[number] == 'N' || player_1[number] == 'R'
             || player_1[number] == 'S' || player_1[number] == 'T' || player_1[number] == 'U')
            {
                counter_1 += 1;
            }
            else if (player_1[number] == 'D' || player_1[number] == 'G')
            {
                counter_1 += 2;
            }
            else if (player_1[number] == 'B' || player_1[number] == 'C' || player_1[number] == 'M' || player_1[number] == 'P')
            {
                counter_1 += 3;
            }
            else if (player_1[number] == 'F' || player_1[number] == 'H' || player_1[number] == 'V' || player_1[number] == 'W' || player_1[number] == 'Y')
            {
                counter_1 += 4;
            }
            else if (player_1[number] == 'K')
            {
                counter_1 += 5;
            }
            else if (player_1[number] == 'J' || player_1[number] == 'X')
            {
                counter_1 += 8;
            }
            else if (player_1[number] == 'Q' || player_1[number] == 'Z')
            {
                counter_1 += 10;
            }
        }

    }
    printf("%i\n", counter_1);

}
