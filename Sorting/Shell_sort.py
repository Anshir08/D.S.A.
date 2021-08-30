a = [5, 4, 8, 3, 4, 14, 90, 45, 9, 3, 2, 4]
gap = len(a)//2
while gap>0:
    for i in range(gap,len(a)):
        temp = a[i]
        j = i
        while j >= gap and temp < a[j-gap]:
            a[j] = a[j-gap]
            j = j-gap
        a[j] = temp
    gap = gap//2
print(a)