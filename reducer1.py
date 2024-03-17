import sys

# Initialize variables to store previous and current word counts
previous_word = None
previous_count = 0
current_word = None

# Read input from standard input (STDIN)
for line in sys.stdin:
    # Strip whitespace and split the line into word and count
    line = line.strip()
    current_word = line.split('\t')[0]
    count = 1

    # If the current word is the same as the previous word, update the count
    if previous_word == current_word:
        previous_count += int(count)
    else:
        # If the current word is different from the previous word,
        # print the previous word and its count
        if previous_word:
            print(f'{previous_word}\t{previous_count}')
        # Reset the count and update the previous word to the current word
        previous_count = count
        previous_word = current_word

# Print the last word and its count
if previous_word == current_word:
    print(f'{previous_word}\t{previous_count}')
dded to explain each part of the code.