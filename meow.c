#include <stdio.h>

void meow(void);

int main(void)
{
    meow(3);
}

void meow(int n)
{
    for (int i = 0; i < n; i += 1)
    {
        printf("meow\n");
    }

}
