#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Deklarerer funktioner til at validere nøgle og erstatte tegn
bool is_valid_key(string key);
char substitute(char c, string key);

int main(int argc, string argv[])
{
    // Tjekker, at programmet er startet med præcis ét argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;  // Afslut programmet, hvis der er fejl i input
    }

    // Gemmer nøglen fra programargumentet
    string key = argv[1];

    // Validerer nøglen
    if (!is_valid_key(key))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;  // Afslut programmet, hvis nøglen er ugyldig
    }

    // Får input fra brugeren i form af tekst, der skal krypteres
    string plaintext = get_string("plaintext: ");

    // Udskriver begyndelsen af krypteret tekst
    printf("ciphertext: ");

    // Gennemløber hvert tegn i teksten
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // Udskriver det krypterede tegn
        printf("%c", substitute(plaintext[i], key));
    }
    printf("\n");

    return 0;
}

// Funktion til at validere nøglen
bool is_valid_key(string key)
{
    // Tjekker, om nøglen har præcis 26 tegn
    if (strlen(key) != 26)
    {
        return false;  // Returner falsk, hvis nøglen ikke er 26 tegn lang
    }

    bool seen[26] = {false};  // Array til at holde styr på unikke bogstaver

    // Gennemgår hvert tegn i nøglen
    for (int i = 0; i < 26; i++)
    {
        // Hvis tegn ikke er et bogstav, returneres falsk
        if (!isalpha(key[i]))
        {
            return false;
        }

        // Konverterer til stor bogstav og beregner position i alfabetet
        int index = toupper(key[i]) - 'A';

        // Hvis bogstavet allerede er set, er der en duplikat
        if (seen[index])
        {
            return false;  // Returner falsk, hvis der er dubletter
        }
        seen[index] = true;  // Markerer bogstavet som set
    }

    return true;  // Returner sand, hvis nøglen er gyldig
}

// Funktion til at erstatte hvert tegn med et tilsvarende tegn i nøglen
char substitute(char c, string key)
{
    // Tjekker, om tegnet er en bogstav
    if (isalpha(c))
    {
        // Bevarer om tegnet er stort eller småt
        bool is_upper = isupper(c);

        // Finder placeringen af tegnet i alfabetet
        int index = toupper(c) - 'A';

        // Returnerer det tilsvarende bogstav i nøglen med korrekt case
        return is_upper ? toupper(key[index]) : tolower(key[index]);
    }
    else
    {
        return c;  // Ikke-bogstavtegn forbliver uændret
    }
}
