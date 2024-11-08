#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;

    // Bed brugeren om et positivt beløb for change
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Start med antal mønter på nul
    int coins = 0;

    // Udregn antallet af quarters
    coins += cents / 25;
    cents %= 25;

    // Udregn antallet af dimes
    coins += cents / 10;
    cents %= 10;

    // Udregn antallet af nickels
    coins += cents / 5;
    cents %= 5;

    // Udregn antallet af pennies
    coins += cents / 1;

    // Print total antal mønter
    printf("%i\n", coins);
}
