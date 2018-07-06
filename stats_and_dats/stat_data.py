from numpy import std, dot, correlate

with open("random1.data", 'r') as input:
    data1 = list()
    for line in input:
        data1.extend([int(x) for x in line.replace('[', '').replace(']', '').split()])

data1avg = sum(data1) / len(data1)
data1stddev = std(data1)

print("Data 1:")
print("Average: " + str(data1avg))
print("Standard Dev: " + str(data1stddev))

with open("random2.data", 'r') as input:
    data2 = list()
    for line in input:
        data2.extend([int(x) for x in line.replace('[', '').replace(']', '').split()])

data2avg = sum(data2) / len(data2)
data2stddev = std(data2)

print("\nData 2:")
print("Average: " + str(data2avg))
print("Standard Dev: " + str(data2stddev))

cov = dot(data1, data2) / len(data1)

cor = cov / data1stddev / data2stddev

print("\nCorrelation: " + str(cor))