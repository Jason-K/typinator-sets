# parseWordlist.py

import datetime

# List of substrings to search for in each word
substrings = ["mnet", "emnt", "wiht", "otu",
              "teh", "hte", "edn", "hso", "lwo", "ign", "ei" ]

# File paths (assuming the script is run from the same folder as the wordlist)
input_file = "Source/words_alpha.txt"

# Generate the output file name with the current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
output_file = f"PCRE exceptions - v.{timestamp}.txt"

# Concatenate substrings for the header comment in all caps and wrapped in quotes
substrings_comment = ", ".join(f'"{sub.upper()}"' for sub in substrings)

# Open the input file for reading and the output file for writing
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    seen_words = set()  # Set to track unique words
    for line in infile:
        word = line.strip()  # Remove any leading/trailing whitespace/newlines
        if word:  # Ignore blank lines
            # Check if any of the specified substrings is in the word
            if any(sub in word for sub in substrings):
                seen_words.add(word)  # Add unique words to the set

    # Write the header comment
    outfile.write(f"# EXCEPTIONS FOR PCRE RULES THAT CORRECT {substrings_comment}\n")

    # Write the sorted unique words to the output file
    for word in sorted(seen_words):
        outfile.write(word + "\t" + word + "\n")
