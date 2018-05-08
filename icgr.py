#############################################################################
# Author: Muhammed S. ElRakabawi (elrakabawi.github.io)
# Paper: Yin, C. (2017). Encoding DNA sequences by integer chaos game representation
# License: MIT
#############################################################################


file = open('input.txt', 'r')                                                   # Open The file containing input
seq = file.read()                                                               # Reading DNA sequence


def clean_file(this_file):                                                      # Truncating function for cleaning the file
    this_file.seek(0)                                                           # Point cursor to first line
    this_file.truncate()                                                        # Truncate file
    this_file.seek(0)                                                           # Return cursor to first line
    return this_file


def encode_icgr(dna_seq):                                                       # Integer Chaos Game Representation Encoder
    i_value = 0                                                                 # base index (position)
    alpha_x = 0                                                                 # Alpha (i,x)
    alpha_y = 0                                                                 # Alpha (i,y)
    arr = []                                                                    # List of lists [(i,Xi,Yi)..(n, X, Yn)]
    cgr_coordinate = {'A': (1, 1), 'G': (1, -1), 'T': (-1, 1), 'C': (-1, -1)}   # Base mapping to coordinates

    for n in seq:                                                               # For every nucleotide in sequence
        i_value = i_value + 1                                                   # increment i --> n
        alpha_x = cgr_coordinate[n][0]                                          # alpha_x = Nucleotide Xi coordinate
        alpha_y = cgr_coordinate[n][1]                                          # alpha_y = Nucleotide Yi coordinate

        if i_value == 1:
            px = (2 ** (i_value - 1)) * alpha_x
            py = (2 ** (i_value - 1)) * alpha_y
        elif i_value > 1:
            px = px + (2 ** (i_value - 1)) * alpha_x
            py = py + (2 ** (i_value - 1)) * alpha_y

        arr.append([i_value, alpha_x, alpha_y, px, py])

        big_x_value = arr[len(arr) - 1][3]
        big_y_value = arr[len(arr) - 1][4]

    return i_value, big_x_value, big_y_value


def decode_icgr(i_value, big_x, big_y):                                         # Integer Chaos Game Representation Decoder
    arr = []                                                                    # List of Bases [(i,Xi,Yi)..(n, X, Yn)]
    cgr_coordinate = {(1, 1): 'A', (1, -1): 'G', (-1, 1): 'T', (-1, -1): 'C'}   # Coordinates mapping back to Bases
    alpha_x = 0
    alpha_y = 0

    for step in range(i_value, 0, -1):                                          # For Every step in range (i --> 0)
        if big_x > 0:
            alpha_x = 1
        elif big_x < 0:
            alpha_x = -1

        if big_y > 0:
            alpha_y = 1
        elif big_y < 0:
            alpha_y = -1

        big_x = (abs(big_x)-(2**(i_value-1)))*alpha_x                           # [|Pi,x| - 2^(i-1)] * alpha(i,x)
        big_y = (abs(big_y) - (2 ** (i_value - 1))) * alpha_y                   # [|Pi,y| - 2^(i-1)] * alpha(i,y)
        arr.append(cgr_coordinate[(alpha_x, alpha_y)])
        i_value -= 1

    decoded_seq = ''.join(arr[::-1])                                            # Reverse and join chars to a string

    return decoded_seq                                                          # Return Decoded Sequence


answer_file = open('output.txt', 'a')                                           # Open the file containing output
answer_file = clean_file(answer_file)                                           # Truncate the file
encoded = encode_icgr(seq)
answer_file.write(str(encode_icgr(seq)))

print('ICGR Encoding Done --> output.txt\n\n', 'i:', encoded[0], ', X:', encoded[1], ', Y:', encoded[2])

x = decode_icgr(encoded[0], encoded[1], encoded[2])
seq += 'A'
print(x, seq)

if x == seq:
    print('Right!')
else:
    print('Wrong')