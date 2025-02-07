arr = [23,2,34,5,1,6]
minindex = 0
temp = 0
for i in range (len(arr)):
    minindex = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[minindex]:
            minindex = j
    temp = arr[i]
    arr[i] = arr[minindex]
    arr[minindex] = temp

print(arr)