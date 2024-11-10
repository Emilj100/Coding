#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input: ");
    prinf("Output: ");
    for (int i = 0; i < strlen(s); i += 1)
    {
        prinf("%c", s[i]);
    }
    printf("\n");

}


