def insertion_sort(arr):
    if len(arr) < 2:
        return
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] <= key:
                break
            arr[j+1] = arr[j]
        arr[j+1] = key
        print(arr)


data = [12, 11, 13, 5, 6, 9, 8]
insertion_sort(data)
print(data)

