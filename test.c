#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// Funktion, der tjekker, om en streng kun består af cifre
bool only_digits(string s);

// Funktion, der roterer et tegn med en given nøgle
char rotate(char c, int key);

int main(int argc, string argv[])
{
    // Tjekker, om antallet af argumenter er korrekt (dvs. kun ét argument udover programmets navn)
    if (argc != 2)
    {
        // Udskriver en fejlmeddelelse og returnerer 1 for at signalere en fejl
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Tjekker, om argumentet kun består af cifre
    if (!only_digits(argv[1]))
    {
        // Udskriver en fejlmeddelelse og returnerer 1 for at signalere en fejl
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Konverterer nøgleargumentet fra streng til heltal
    int key = atoi(argv[1]);

    // Prompt brugeren for plaintext-input
    string plaintext = get_string("plaintext: ");

    // Udskriver starten på ciphertext-output
    printf("ciphertext: ");

    // Gennemløber hvert tegn i brugerens input
    for (int i = 0; i < strlen(plaintext); i++)
    {
        // Roterer tegnene og udskriver det krypterede tegn
        printf("%c", rotate(plaintext[i], key));
    }

    // Udskriver newline efter ciphertext
    printf("\n");

    // Returnerer 0 for at signalere succes
    return 0;
}

// Funktion, der tjekker, om en streng kun består af cifre
bool only_digits(string s)
{
    // Gennemgår hvert tegn i strengen
    for (int i = 0; s[i] != '\0'; i++)
    {
        // Hvis tegnet ikke er et ciffer, returner false
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    // Returner true, hvis alle tegn er cifre
    return true;
}

// Funktion, der roterer et bogstav baseret på nøgleværdien
char rotate(char c, int key)
{
    // Tjekker, om tegnet er et bogstav
    if (isalpha(c))
    {
        // Bestemmer, om tegnet er stort eller lille
        char base = isupper(c) ? 'A' : 'a';
        // Beregner ny position og returnerer det roterede tegn
        return (c - base + key) % 26 + base;
    }
    else
    {
        // Returnerer uændrede tegn, hvis de ikke er bogstaver
        return c;
    }
}
