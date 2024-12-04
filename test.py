import csv
import sys


def main():
    # Check for correct usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Load the database
    database = []
    with open(sys.argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        database = list(reader)

    # Extract STRs from the header
    strs = reader.fieldnames[1:]

    # Load the DNA sequence
    with open(sys.argv[2], "r") as txtfile:
        sequence = txtfile.read()

    # Find the longest match for each STR in the sequence
    str_counts = {str_: longest_match(sequence, str_) for str_ in strs}

    # Compare against each person in the database
    for person in database:
        if all(int(person[str_]) == str_counts[str_] for str_ in strs):
            print(person["name"])
            return

    # If no match is found
    print("No match")


def longest_match(sequence, subsequence):
    """
    Returns the length of the longest run of a subsequence in the sequence.
    """
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    # Iterate through the sequence
    for i in range(seq_len):
        count = 0

        # Count consecutive runs of the subsequence
        while sequence[i + count * subseq_len:i + (count + 1) * subseq_len] == subsequence:
            count += 1

        # Update the longest run found
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
