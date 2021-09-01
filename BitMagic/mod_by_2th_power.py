def getModulo(n, d):

    return n & (d-1)

n = 14
d = 8
print(getModulo(n, d))