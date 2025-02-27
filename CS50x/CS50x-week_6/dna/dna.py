import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Please input CSV file and text file")
        sys.exit()
    csv_file = sys.argv[1]
    text_file = sys.argv[2]

    # TODO: Read database file into a variable
    rows = []
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    strs = reader.fieldnames[1:]

    # TODO: Read DNA sequence file into a variable
    with open(text_file) as file:
        read_data = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    str_counts = {}
    for str in strs:
        str_counts[str] = longest_match(read_data, str)

    # Check database for matching profiles
    match_found = False
    for person in rows:
        if all(int(person[str]) == str_counts[str] for str in strs):
            print(person["name"])
            match_found = True
            break
        
    if not match_found:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
