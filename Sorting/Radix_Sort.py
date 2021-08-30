def countingSort(arr, exp):
    count = [0]*10
    n = len(arr)
    output = [0]*n

    for i in range(n):
        index = arr[i]//exp
        count[index%10] += 1

    for i in range(1,n):
        count[i] += count[i-1]
    
    # for i in arr:
    #     output[count[i]-1] = i
    #     count[i] -= 1

    for i in range(n-1,-1,-1):
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]
 

def radixSort(arr):
    m = max(arr)
    exp = 1
    while m//exp > 0:
        countingSort(arr, exp)
        exp *= 10


if __name__ == '__main__':
    arr = [5, 13, 101, 6, 7, 11, 12, 100]
    radixSort(arr)
    print(arr)