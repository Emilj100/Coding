#include <stdio.h>

int main(void)
{
    int scores[1024];
    for (int i = 0; i < 1024; i += 1)
    {
        printf("%i\n", scores[i]);
    }
}
