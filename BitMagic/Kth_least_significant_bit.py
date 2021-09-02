def KthLSB(n, k):

    return (n>>(k-1))&1

if __name__ == '__main__':
    n = 10
    k = 4
    print(KthLSB(n, k))