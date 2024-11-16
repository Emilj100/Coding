#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Maksimalt antal vælgere og kandidater
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] er vælger i's j-te præference
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Kandidater har navn, stemmeantal og elimineringsstatus
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array af kandidater
candidate candidates[MAX_CANDIDATES];

// Antal vælgere og kandidater
int voter_count;
int candidate_count;

// Funktion prototyper
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Tjek for gyldig brug
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Udfyld kandidat-arrayet
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    // Indhent antal vælgere
    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Hent vælgernes præferencer
    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }
    }

    // Afhold løbende valg
    while (true)
    {
        // Beregn stemmer for ikke-eliminerede kandidater
        tabulate();

        // Tjek, om der er en vinder
        if (print_winner())
        {
            break;
        }

        // Find kandidat med færrest stemmer
        int min = find_min();

        // Tjek, om der er uafgjort
        if (is_tie(min))
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminer kandidater med færrest stemmer
        eliminate(min);

        // Nulstil stemmeantal
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Registrer en gyldig stemme
bool vote(int voter, int rank, string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Beregn stemmer for ikke-eliminerede kandidater
void tabulate(void)
{
    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            int candidate_index = preferences[i][j];
            if (!candidates[candidate_index].eliminated)
            {
                candidates[candidate_index].votes++;
                break;
            }
        }
    }
}

// Udskriv vinderen, hvis der er en
bool print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes > voter_count / 2)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }
    return false;
}

// Find mindste stemmeantal blandt kandidaterne
int find_min(void)
{
    int min_votes = MAX_VOTERS;
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes < min_votes)
        {
            min_votes = candidates[i].votes;
        }
    }
    return min_votes;
}

// Tjek om der er uafgjort mellem alle tilbageværende kandidater
bool is_tie(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes != min)
        {
            return false;
        }
    }
    return true;
}

// Eliminer kandidater med færrest stemmer
void eliminate(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
}
