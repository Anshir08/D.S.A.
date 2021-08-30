import Insertion_Sort

def bucketSort(x):
    arr = []
    
    for i in range(10):
        arr.append([])

    for j in x:
        index = int(j*10)
        arr[index].append(j)

    for i in range(10):
        arr[i] = Insertion_Sort.sort(arr[i])
    
    y = []
    for i in arr:
        if len(i)>0:
            y.extend(i) 

    return y

if __name__ == '__main__':
    x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
    print(bucketSort(x))