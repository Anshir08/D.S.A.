arr = [5, 13, 6, 7, 11, 12]
count, Csort = [0]*(max(arr)+1), [0]*len(arr)
for i in arr:
    count[i] += 1
for i in range(1,len(count)):
    count[i] += count[i-1]
for i in arr:
    Csort[count[i]-1] = i
    count[i] -= 1
print(Csort)