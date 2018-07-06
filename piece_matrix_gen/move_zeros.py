all_moves = list()

line_num = 1

with open("princessmoves.txt", "r") as file:
    for line in file:
        #skip the commented lines
        if line_num < 5:
            line_num += 1
            continue
        #blank rows, cannot move from here
        elif (30 <= line_num <= 34) or (38 <= line_num <= 42):
            moves = [0] * 24
        #normal rows
        else:
            moves = list()
            line_ints = [int(s) for s in line.split()]
            for move in line_ints:
                x = (int(move) - 1) % 8 + 1
                y = ((int(move) - 1) // 8) + 1
                #if move is to a valid square, add it
                if int(move) != 0 and (int(move) < 26 or 31 <= int(move) <= 33 or int(move) > 38):
                    moves.append(move)


            if len(moves) != 0:
                for i in range(len(moves), 24):
                    moves.append(0)

        all_moves.append(moves)

        line_num += 1

with open("princessmoves_mod.txt", "w", newline='\n') as file:
    file.write("# name: princessmoves_mod\n")
    file.write("# type: global matrix\n")
    file.write("# rows: 64\n")
    file.write("# columns: 24\n")
    for line in all_moves:
        for s in line:
            file.write(str(s) + " ")
        file.write("\n")

print(all_moves)