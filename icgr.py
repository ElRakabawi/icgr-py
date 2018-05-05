seq = input()

i_value = 0
alpha_x = 0
alpha_y = 0

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

    i_value = i_value + 1
    print(n, 'i is: ', i_value, ', x: ', alpha_x, ', y: ', alpha_y)



