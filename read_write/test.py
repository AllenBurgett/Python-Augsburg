file = open("shakespeare-hamlet-25.txt", 'r')
for line in file:
    for word in line.split():
        print(word)