rows = 64
cols = 24

all_moves = list()

#linear iteration through board
for sqr in range(1, 65):
    #convert to (x, y)
    x = (sqr - 1) % 8 + 1
    y = ((sqr - 1) // 8) + 1
    moves = list()

    #row movement
    for i in range(-3, 4):
        if 0 < (x + i) < 9 and i != 0:
            move = ((x + i), y)
            square = (move[1] - 1) * 8 + (move[0] - 1) + 1
            moves.append(square)

    #column movement
    for i in range(-3, 4):
        if 0 < (y + i) < 9 and i != 0:
            move = (x, (y + i))
            square = (move[1] - 1) * 8 + (move[0] - 1) + 1
            moves.append(square)

    #diagonal movement
    for i in range(-3, 4):
        if (0 < (x + i) < 9) and (0 < (y + i) < 9) and i != 0:
            move = ((x + i), (y + i))
            square = (move[1] - 1) * 8 + (move[0] - 1) + 1
            moves.append(square)

        if (0 < (x + i) < 9) and (0 < (y - i) < 9) and i != 0:
            move = ((x + i), (y - i))
            square = (move[1] - 1) * 8 + (move[0] - 1) + 1
            moves.append(square)

    #fill blank columns
    for i in range(len(moves), cols):
        moves.append(0)

    all_moves.append(moves)

with open("princessmoves.txt", "w", newline='\n') as file:
    file.write("# name: princessmoves\n")
    file.write("# type: global matrix\n")
    file.write("# rows: " + str(rows) + "\n")
    file.write("# columns: " + str(cols) + "\n")
    for line in all_moves:
        for s in line:
            file.write(str(s) + " ")
        file.write("\n")