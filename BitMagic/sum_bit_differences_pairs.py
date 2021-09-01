def sumBitDifferences(arr, n):
 
    ans = 0
 
    # traverse over all bits
    for i in range(0, 32):
     
        count = 0
        for j in range(0, n):
            if ( (arr[j] & (1 << i)) ):
                count+= 1
 
        ans += (count * (n - count) * 2);
     
    return ans
 
# Driver prorgram
arr = [1, 3, 5]
n = len(arr )
print(sumBitDifferences(arr, n))