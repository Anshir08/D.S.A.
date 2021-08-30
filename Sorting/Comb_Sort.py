def  combSort(arr):
    n = len(arr)
    gap = n
    while gap//1.3 > 1:
        for i, j in zip(range(0,n-gap+1),range(gap-1,n)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        gap = round(gap/1.3)
    for i, j in zip(range(0,n-1),range(1,n)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    combSort(arr)
    print(arr)