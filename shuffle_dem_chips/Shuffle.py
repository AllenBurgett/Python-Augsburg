import fileinput

def main():
    in_file = fileinput.input()

    stacknum = int(in_file.readline())

    sets = list()
    for i in range(stacknum):
        c = int(in_file.readline())
        s1 = in_file.readline()
        s2 = in_file.readline()
        result = in_file.readline()
        sets.append([c, s1, s2, result])

    for i in range(len(sets)):
        c = sets[i][0]
        s1 = sets[i][1].strip()
        s2 = sets[i][2].strip()
        result = sets[i][3].strip()
        shuffle_num = 0
        s1_ori = s1
        s2_ori = s2
        while(s1 + s2 != result):
            s1, s2 = shuffle(c, s1, s2)
            if s1 == s1_ori and s2 == s2_ori:
                shuffle_num = -1
                break
            shuffle_num += 1
        print(str(i + 1) + " " + str(shuffle_num))

def shuffle(c, s1, s2):
    combined = ""
    for i in range(c):
        combined = combined + s2[i] + s1[i]

    s1 = combined[:c]
    s2 = combined[c:]

    return s1, s2

main()