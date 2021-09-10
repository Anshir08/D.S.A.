def printMaximum(num):
    d = {}
    for i in range(10):
        d[i] = 0
    
    for i in str(num):
        d[int(i)] += 1

    res = 0
    m = 1
    for i in list(d.keys()):
        while d[i] > 0:
            res = res + i*m
            d[i] -= 1
            m *= 10
    return res
    
# Driver code
num = 38293367
print(printMaximum(num))