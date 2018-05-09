#############################################################################
# Author: Muhammed S. ElRakabawi (elrakabawi.github.io)
# Paper: Yin, C. (2017). Encoding DNA sequences by integer chaos game representation
# License: MIT
#############################################################################
import argparse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


parser = argparse.ArgumentParser(description='Integer Chaos Game Representation of DNA Encoder/Decoder script')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encode', type=str, help='Encode sequence from fasta file')
group.add_argument('-d', '--decode', type=str, help='Decode sequence from icgr file')
parser.add_argument('-q', '--quiet', action='store_true', help='Will not print validity checks')
args = parser.parse_args()

################################ FUNCTIONS ###################################


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

    for n in dna_seq:                                                               # For every nucleotide in sequence
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


################################ CORE LOGIC ###################################

if args.encode:
    fastapath = args.encode
    icgrpath = fastapath[:fastapath.find('.')] + '.icgr'
    seq_comments = []
    fasta_seq = ''
    with open(fastapath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if line[0] == '>':
                seq_desc = line
            elif line[0] == ';':
                seq_comments.append([line])
            else:
                line = line.replace('\n', '')
                fasta_seq += line
            line = fp.readline()

        seq_desc = '>>{}'.format(seq_desc)
        encoded_seq = encode_icgr(fasta_seq)

        decoded_seq = decode_icgr(encoded_seq[0], encoded_seq[1], encoded_seq[2])
        answer_file = open(icgrpath, 'a')
        answer_file = clean_file(answer_file)

        answer_file.write(seq_desc)
        answer_file.write(str(encoded_seq))

        if not args.quiet:
            print(bcolors.HEADER, 'Script running in Verbose Mode.\n Validity checks will be printed!', bcolors.ENDC)
            print(' Fasta file path:', fastapath)
            if decoded_seq == fasta_seq:
                print(bcolors.OKBLUE, 'Validity check returns True.', bcolors.ENDC)
                print(bcolors.OKBLUE, 'ICGR Encoding Done (Trusted) --> ', icgrpath, bcolors.ENDC, '\nI:',
                      encoded_seq[0], '\nX:', encoded_seq[1], '\nY:', encoded_seq[2])
            else:
                print(bcolors.WARNING, 'Validity check returns False.', bcolors.ENDC)
                choice = input(' Output file anyway? [y]: ')
                if choice == 'y':
                    print(bcolors.OKBLUE, 'ICGR Encoding Done (Not Trusted) --> ', icgrpath, bcolors.ENDC, '\n I:',
                          encoded_seq[0], '\n X:', encoded_seq[1], '\n Y:', encoded_seq[2])
                else:
                    print(bcolors.FAIL, 'iCGR encoding was not completed due to internal error', bcolors.ENDC)

        elif args.quiet:
            print(bcolors.HEADER, 'Script running in Quiet Mode.', bcolors.ENDC)
            if decoded_seq == fasta_seq:
                print(bcolors.OKBLUE, 'ICGR Encoding Done (Trusted) --> ', icgrpath, bcolors.ENDC)
            else:
                print(bcolors.WARNING, 'ICGR Encoding Done (Not Trusted) --> ', icgrpath, bcolors.ENDC)

elif args.decode:
    file = open(args.decode, 'r')
    icgr = file.read()
    print(icgr)

