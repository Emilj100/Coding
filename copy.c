#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char *s = get_string("s: ");

    char *t = malloc(strlen(s) + 1);

    for (int i = 0, n = strlen(s); i < n i += 1)
    {
        t[i] = s[i];
    }

    t[1] = toupper(t[1]);

    printf("%s\n", s);
    printf("%s\n", t);
}
