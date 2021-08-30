from collections import defaultdict


def sort_0_1_2(arr):

    d = defaultdict(lambda: 0)
    for i in arr:
        d[arr[i]] += 1
    
    return sum([[i]*d[i] for i in sorted(d.keys())], [])
    
    
if __name__ == '__main__':
    arr = [0,1,2,0,1,2]
    print(sort_0_1_2(arr))
    