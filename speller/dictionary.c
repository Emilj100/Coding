// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1009;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int length = strlen(word);

    int hashvalue = 0;
    for (int i = 0; i < length; i++)
    {
        int hash = toupper(word[i]) - 'A';
        hashvalue += hash;

    }
    return hashvalue % N;

}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    char buffer[46];
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }


    node *list = NULL;
    while (fscanf(source, "%s", buffer) == 1)
    {

        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, buffer);
        int hashvalue = hash(n->word);
        printf("Indlæser ord: %s i bucket: %i\n", buffer, hashvalue);
        n->next = table[hashvalue];
        table[hashvalue] = n;

    }

    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
