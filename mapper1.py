import sys

# Read entire line from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Assign count one to each word 
    for word in words:
        word = word.replace('\"', "")
        word = word.replace(",", "")
        word = word.replace(";", "")
        word = word.replace("!", "")
        word = word.replace("-", "")
        word = word.replace("_", "")
        word = word.replace("?", "")
        word = word.replace("|", "")
        print(f'{word}\t{1}')
