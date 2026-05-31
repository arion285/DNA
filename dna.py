import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: Incorrect Command")
        sys.exit(1)

    # TODO: Read database file into a variable
    database = []
    with open(f"{sys.argv[1]}") as file:
        # Read dictionary headers/keys (first row) into reader with each of the headers acting as keys later on
        reader = csv.DictReader(file)
        # associate or maps every data in each row to a dictionary above with the headers (keys) above
        for row in reader:
            database.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(f"{sys.argv[2]}") as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # list of subsequences
    subsequences = list(database[0].keys())[1:]
    # calculation of each subsequence from the DNA sequence
    outcome = {}
    for subsequence in subsequences:
        outcome[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    for person in database:
        match = 0
        # print(match)
        for subsequence in subsequences:
            if int(person[subsequence]) == outcome[subsequence]:
                match += 1
            # print(person[subsequence], end="")
        # print()
        # print(match)
        if match == len(subsequences):
            print(person['name'])
            return

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

# Ready for review
