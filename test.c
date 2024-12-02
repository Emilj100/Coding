// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Define number of buckets in the hash table
const unsigned int N = 1009;

// Hash table
node *table[N];

// Global variable to count words in dictionary
int word_count = 0;

// Hash function
unsigned int hash(const char *word)
{
    unsigned int hashvalue = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hashvalue = (hashvalue * 31) + toupper(word[i]);
    }
    return hashvalue % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer to store words
    char buffer[LENGTH + 1];

    // Read words from dictionary
    while (fscanf(file, "%s", buffer) != EOF)
    {
        // Create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(file);
            return false;
        }

        // Copy word into node
        strcpy(n->word, buffer);

        // Hash the word to get a bucket index
        unsigned int index = hash(buffer);

        // Insert node into the linked list at that index
        n->next = table[index];
        table[index] = n;

        // Increment word count
        word_count++;
    }

    // Close dictionary file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash word to get bucket index
    unsigned int index = hash(word);

    // Traverse the linked list at that index
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // Compare words case-insensitively
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    // If word not found, return false
    return false;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        // Free all nodes in the linked list at table[i]
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }

    return true;
}
