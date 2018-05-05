# Open The file containing input
file = open('input.txt', 'r')
seq = file.read()

i_value = 0
alpha_x = 0
alpha_y = 0


def clean_file(this_file):
    this_file.seek(0)
    this_file.truncate()
    this_file.seek(0)

    return this_file


answer_file = open('output.txt', 'a')
answer_file = clean_file(answer_file)

for n in seq:
    if n == 'A':
        alpha_x = 1
        alpha_y = 1
    elif n == 'T':
        alpha_x = -1
        alpha_y = 1
    elif n == 'C':
        alpha_x = -1
        alpha_y = -1
    elif n == 'G' :
        alpha_x = 1
        alpha_y = -1

    cor = str(n) + 'i is: ' + str(i_value) + ', x: ' + str(alpha_x) + ', y: ' + str(alpha_y) + '\n'
    answer_file.write(cor)
