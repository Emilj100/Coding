#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// Funktioner, der tjekker om et input kun består af tal, og som roterer bogstaver
bool only_digits(string s);
char rotate(char c, int key);

int main(int argc, string argv[])
{
    // Tjekker om der er præcis to argumenter (programmet + nøglen)
    if (argc != 2)
    {
        // Hvis ikke, print en brugervejledning og afslut programmet
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Tjekker om nøglen kun består af tal
    if (!only_digits(argv[1]))
    {
        // Hvis ikke, print en brugervejledning og afslut programmet
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Konverterer nøglen fra string til int
    int offset = atoi(argv[1]);
    // Få input fra brugeren for den tekst, der skal krypteres
    string input = get_string("plaintext: ");

    // Definerer alfabetet og antallet af bogstaver
    const string lower = "abcdefghijklmnopqrstuvwxyz";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const int max = 26;

    // Print overskrift for den krypterede tekst
    printf("ciphertext: ");
    // Gennemløber hvert tegn i brugerens input
    for (int i = 0; i < strlen(input); i++)
    {
        // Gemmer det aktuelle tegn
        char current = input[i];
        // Tjekker om tegnet er et bogstav
        if (isalpha(current))
        {
            // Bestemmer om tegnet er stort eller lille bogstav
            char base = isupper(current) ? 'A' : 'a';
            // Beregner den nye position ved at tage forskydning med nøglen
            int idx = (current - base + offset) % max;
            // Udskriver det krypterede bogstav (stort eller lille afhængigt af originalen)
            printf("%c", isupper(current) ? upper[idx] : lower[idx]);
        }
        else
        {
            // Hvis tegnet ikke er et bogstav, udskrives det som det er
            printf("%c", current);
        }
    }

    // Ny linje efter den krypterede tekst
    printf("\n");
    return 0;
}

// Funktion der tjekker om et input kun indeholder cifre
bool only_digits(string s)
{
    // Gennemgår hvert tegn i strengen
    for (int i = 0; s[i] != '\0'; i++)
    {
        // Hvis tegnet ikke er et ciffer, returneres false
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    // Returnerer true, hvis alle tegn er cifre
    return true;
}
