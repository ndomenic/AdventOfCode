import sys
import math

f = open(sys.argv[1], "r")
sum = 0

for line in f:
  sum += math.floor(int(line)/3)-2

print("Sum: " + str(sum))