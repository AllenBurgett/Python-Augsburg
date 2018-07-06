from numpy import random

out_file = open("random1.data", 'w')
numlist = random.random_integers(1, 10001, 1000)
out_file.write(str(numlist))
out_file.close()

out_file = open("random2.data", 'w')
numlist = random.random_integers(150, 10501, 1000)
out_file.write(str(numlist))
out_file.close()
