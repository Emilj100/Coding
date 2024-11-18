#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = s;

    t[1] = toupper(t[1]);

    printf("%s\n", s);
    printf("%s\n", t);
}
