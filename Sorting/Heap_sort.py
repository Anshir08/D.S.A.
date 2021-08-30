def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and arr[largest] < arr[l]:
        largest = l
    
    if r<n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    print(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# arr = [5, 4, 8, 3, 4, 14, 90, 45, 9, 3, 2, 4]
# heapSort(arr)
# print(arr)
arr = [5, 13, 6, 7, 11, 12]
heapSort(arr)
print(arr)