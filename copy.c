#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    string s = get_string("s: ");
    string t = s;

    t[1] = toupper(t[1]);

    printf("%s\n", s);
    printf("%s\n", t);
}
