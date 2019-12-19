begin = 124075
end = 580769
counter = 0

arr = []
for i in range(10):
    arr.append(0)

for i in range(begin, end):
    string = str(i)

    for j in range(10):
        arr[j] = 0

    lastInt = string[0]
    arr[int(lastInt)] += 1
    decrease = False

    for j in range(1, len(string)):
        arr[int(string[j])] += 1
            
        if (lastInt > string[j]):
            decrease = True

        lastInt = string[j]

    if (not decrease):
        for k in range(10):
            if (arr[k] == 2):
                counter += 1
                break

print (counter)