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
    // i starter med at være 0. Loopet skal køre imens i er mindre end n. I hver iteration tilføjer vi +1 til i.
    for (int i = 0; i < n; i += 1)
    {
        // j starter med at være 0. Loopet skal derefter køre indtil at imens at j er mindre end n(brugerens input) - i()
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
