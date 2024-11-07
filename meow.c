#include <stdio.h>

void meow(void);

int main(void)
{
    for (int i = 0; i < 3; i += 1)
    {
        meow();
    }
}

void meow(void)
{
    printf("meow\n");
}
