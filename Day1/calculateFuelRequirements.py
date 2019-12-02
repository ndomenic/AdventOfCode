import sys
import math

def calculateRecursively(num):
    tmpNum = int(math.floor(int(num)/3)-2)
    if (tmpNum >= 0):
        return tmpNum + calculateRecursively(tmpNum)
    return 0

f = open(sys.argv[1], "r")
sum = 0

for line in f:
    sum += calculateRecursively(line)

print("Sum: " + str(sum))