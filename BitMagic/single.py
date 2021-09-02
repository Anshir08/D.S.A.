def findSingle(arr):
    res = arr[0]
    for i in arr[1::]:
        res = res^arr[i]
    return res


arr = [7, 3, 5, 4, 5, 3, 4]
print(findSingle(arr))