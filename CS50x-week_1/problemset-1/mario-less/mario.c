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

    for (int i = n; i > 0; i += 1)



    {


        for (int j = 0; j < n; j += 1)
        {
            printf("#");
        }
        printf("\n");
    }

}
