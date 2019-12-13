import sys
import csv

def populateMap(index):
    x = size-1
    y = 0

    map[index][x][y] = 'O'

    for direction in arr[index]:
        if (direction[0] == 'R'):
            for i in range(int(direction[1])):
                y += 1
                map[index][x][y] = 1
        if (direction[0] == 'L'):
            for i in range(int(direction[1])):
                y -= 1
                map[index][x][y] = 1
        if (direction[0] == 'U'):
            for i in range(int(direction[1])):
                x -= 1
                map[index][x][y] = 1         
        if (direction[0] == 'D'):
            for i in range(int(direction[1])):
                x += 1
                map[index][x][y] = 1

        print(x, y)

arr = []

#read the file into an array
with open(sys.argv[1]) as csvDataFile:
    for row in csv.reader(csvDataFile):
        arr.append(row)

size = 200

#fill the map with 0s in all spots
map = []
map.append([])
map.append([])

for i in range(2):
    for j in range(size):
        map[i].append([])
        for k in range(size):
            map[i][j].append(0)

#add the origin and 1s to track the path of each wire in their maps
populateMap(0)
populateMap(1)

print('')
for i in range(size):           
    print(map[0][i])

print('')
for i in range(size):           
    print(map[1][i])

x = size-1
y = 0

interstions = []

for i in range(size-1, 0, -1): #y
    for j in range(size): #x
        if (map[0][i][j] == 1 and map[1][i][j] == 1):
            interstions.append(size-1-i + j)
            print('intersection!')
            print(map[0][i][j], size-1-i, j)

print(interstions)