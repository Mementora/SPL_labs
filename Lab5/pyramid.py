def create_pyramid(x, y):
    pyramid = []
    for i in range(y):
        line = ''
        for j in range(x):
            if i == 0:  # for the top of the pyramid
                line += '+' if j == x // 2 else ' '
            elif i == y - 1:  # drawing the base of the pyramid
                if j == 0 or j == x - 1:
                    line += '+'  # Place '+' at the beginning and end of the line
                elif j > 0 and j < x - 1:
                    line += '-'  # Fill the middle with '-'
            elif j == x // 2 - i or j == x // 2 + i:  # drawing the edges of the pyramid
                line += '/' if j == x // 2 - i else '\\'
            elif j > x // 2 - i and j < x // 2 + i:  # drawing the sides of the pyramid
                line += ' '
            else:
                line += ' '
        pyramid.append(line)
    return pyramid

pyramid = create_pyramid(30, 15)  # Change the dimensions as needed
for line in pyramid:
    print(line)
