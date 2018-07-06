import os
from glob import glob

currentdir = os.path.abspath('.')
for filename in glob(currentdir + '/*.txt'):
    print(os.path.basename(filename) + ":")
    file = open(filename, 'r')
    file_dict = {}
    for line in file:
        splitLine = line.split()
        for word in splitLine:
            cleanword = word.lower()
            if cleanword in file_dict:
                file_dict[cleanword] += 1
            else:
                file_dict[cleanword] = 1

    sorted_file_dict = sorted(file_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_file_dict[:10])