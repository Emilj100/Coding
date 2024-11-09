#include <stdio.h>          // Inkluderer standardbiblioteket for input og output funktioner.
#include <cs50.h>           // Inkluderer CS50-biblioteket for ekstra funktioner, som get_string.
#include <string.h>         // Inkluderer string.h for at kunne arbejde med tekststrenge.

int main(void)
{
    // Deklarerer en variabel til kortnummeret, som skal gemmes som en tekststreng.
    string card_number;

    // Gentager, indtil brugeren indtaster et gyldigt kortnummer (ikke tomt).
    do
    {
        // Beder brugeren om at indtaste kortnummeret.
        card_number = get_string("Number: ");
    }
    while (card_number == NULL || strlen(card_number) == 0);  // Kontrollerer, at input ikke er tomt.

    // Initialiserer sum til 0 og en tæller for antal cifre.
    int sum = 0;
    int digit_count = 0;

    // Læser kortnummeret baglæns (fra sidste ciffer til første ciffer).
    for (int i = strlen(card_number) - 1; i >= 0; i--)
    {
        // Konverterer det aktuelle tegn i kortnummeret til et heltal.
        int digit = card_number[i] - '0';

        // Hvis cifferet er på en ulige position (hvert andet ciffer fra enden):
        if (digit_count % 2 == 1)
        {
            // Gang cifferet med 2.
            digit *= 2;

            // Hvis resultatet af multiplikationen er større end 9 (to cifre):
            if (digit > 9)
            {
                // Adder cifrene i produktet (f.eks. 12 bliver 1 + 2).
                digit = digit % 10 + 1;
            }
        }

        // Læg cifferets værdi til summen.
        sum += digit;

        // Øger tælleren for antal cifre med 1.
        digit_count++;
    }

    // Efter loopet: Kontroller, om summen slutter på 0 (modulo 10).
    if (sum % 10 == 0)
    {
        // Hvis kortnummeret har 15 cifre og starter med "34" eller "37".
        if ((strlen(card_number) == 15) &&
            (strncmp(card_number, "34", 2) == 0 || strncmp(card_number, "37", 2) == 0))
        {
            printf("amex\n");  // Udskriv "amex" for American Express.
        }
        // Hvis kortnummeret har 16 cifre og starter med "51", "52", "53", "54", eller "55".
        else if ((strlen(card_number) == 16) &&
                 (strncmp(card_number, "51", 2) == 0 || strncmp(card_number, "52", 2) == 0 ||
                  strncmp(card_number, "53", 2) == 0 || strncmp(card_number, "54", 2) == 0 ||
                  strncmp(card_number, "55", 2) == 0))
        {
            printf("mastercard\n");  // Udskriv "mastercard" for Mastercard.
        }
        // Hvis kortnummeret har enten 13 eller 16 cifre og starter med "4".
        else if ((strlen(card_number) == 13 || strlen(card_number) == 16) &&
                 strncmp(card_number, "4", 1) == 0)
        {
            printf("visa\n");  // Udskriv "visa" for Visa.
        }
        else
        {
            printf("invalid\n");  // Udskriv "invalid", hvis kortnummeret ikke matcher noget format.
        }
    }
    else
    {
        printf("invalid\n");  // Udskriv "invalid", hvis summen ikke er gyldig (ikke modulo 10).
    }

    return 0;  // Afslutter programmet med status 0.
}
