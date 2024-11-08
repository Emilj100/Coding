#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Bed brugeren om et positivt tal
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print pyramiden
    for (int i = 0; i < n; i += 1)
    {
        for (int j = 0; j < n - i - 1; j += 1)
        {
            printf(" ");
        }
        for (int f = 0; f < i + 1; f += 1)
        {
            printf("#");
        }
        printf("\n");
    }
}
