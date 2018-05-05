#############################################################################
# Author: Muhammed S. ElRakabawi (elrakabawi.github.io)
# Paper: Yin, C. (2017). Encoding DNA sequences by integer chaos game representation
# License: MIT
#############################################################################


file = open('input.txt', 'r')                                               # Open The file containing input
seq = file.read()                                                           # Reading DNA sequence
i_value = 0                                                                 # nucleotide index (position)
alpha_x = 0                                                                 # Alpha (i,x)
alpha_y = 0                                                                 # Alpha (i,y)
seq_len = len(seq)                                                          # Sequence length
arr = []                                                                    # List of lists [(i,Xi,Yi)..(n, X, Yn)]
cgr_coordinate = {'A': (1, 1), 'G': (1, -1), 'T': (-1, 1), 'C': (-1, -1)}   # Nucleotide mapping to coordinates


#############################################################################
# Functions
#############################################################################


def clean_file(this_file):                                                  # Truncating function for cleaning the file
    this_file.seek(0)                                                       # Point cursor to first line
    this_file.truncate()                                                    # Truncate file
    this_file.seek(0)                                                       # Return cursor to first line
    return this_file


#############################################################################
# File Handling and Core logic
#############################################################################


answer_file = open('output.txt', 'a')                                       # Open the file containing output
answer_file = clean_file(answer_file)                                       # Truncate the file

for n in seq:                                                               # For every nucleotide in sequence
    i_value = i_value + 1                                                   # increment i --> n
    alpha_x = cgr_coordinate[n][0]                                          # alpha_x = Nucleotide Xi coordinate
    alpha_y = cgr_coordinate[n][1]                                          # alpha_y = Nucleotide Yi coordinate
    arr.append([i_value, alpha_x, alpha_y])                                 # Append (i, Xi, Yi) to the list

answer_file.write(str(arr))                                                 # Write the list to the output file
print('\n'.join([''.join(['{:4}'.format(item) for item in row])             # Matrix format for the list [debugging]
                 for row in arr]))