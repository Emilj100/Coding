#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");

    int counter_1 = 0;
    for (int i = 0, n = strlen(player_1); i < n; i += 1)
    {
        if (player_1[i] == 'A' || player_1[i] == 'E' || player_1[i] == 'I' || player_1[i] == 'N' || player_1[i] == 'R' || player_1[i] == 'S' || player_1[i] == 'T' || player_1[i] == 'U')
        {
            counter_1 += 1;
        }

        else if (player_1[i] == 'D' || player_1[i] == 'G')
        {
            counter_1 += 1;
        }

    }
    printf("%i\n", counter_1);

}
