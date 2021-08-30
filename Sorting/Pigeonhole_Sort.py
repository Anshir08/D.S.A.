def pigeonhole_sort(arr):
    Min = min(arr)
    Max = max(arr)
    rng = Max-Min+1

    holes = [[] for _ in range(rng)]
    for i in arr:
        holes[i-Min].append(i)

    output = []
    for i in holes:
        if len(i)>0:
            output.extend(i)
    
    return output

if __name__ == '__main__':
    arr = [5, 4, 8, 3, 4, 14, 90, 45, 9, 3, 2, 4]
    print(pigeonhole_sort(arr))
