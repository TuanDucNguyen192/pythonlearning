arr = [2,4,1,5,10,3]

for i in range (len(arr) - 1):
    for j in range (len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j + 1] = temp

print(arr)