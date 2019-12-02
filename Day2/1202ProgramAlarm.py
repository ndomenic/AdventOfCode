import sys
import csv

arr = []

#read the file into an array
with open(sys.argv[1]) as csvDataFile:
    for row in csv.reader(csvDataFile):
        arr = row

#convert to ints to make life easer
for i in range(len(arr)):
    arr[i] = int(arr[i])

#do the specified modification
arr[1] = 12
arr[2] = 2

for i in range(len(arr)):
    #skip all items that are not operations
    if (i % 4 != 0): 
        continue

    #perform the add operation
    if (arr[i] == 1):
        arr[arr[i + 3]] = arr[arr[i + 1]] + arr[arr[i + 2]]
    #perform the multiply operation
    elif (arr[i] == 2):
        arr[arr[i + 3]] = arr[arr[i + 1]] * arr[arr[i + 2]]
    #exit the loop
    elif (arr[i] == 99):
        break
    
print(arr[0])