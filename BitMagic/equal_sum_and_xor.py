def CountValues(n):

    unset_bits = 0

    while(n):
        # if n^i == n+1 changes 
        # beacause (n+i)=(n^i)+2*(n&i)
        # which implies n&1 = 0 for n+i = n^i
        if n & 1 == 0:
            unset_bits += 1
        n = n >> 1

    # returning 2^unset_bits
    # unset_bits left shift in binary of 1
    return 1 << unset_bits

# Driver's Code
if __name__ == '__main__':
    n = 12
    print(CountValues(n))
# print(8 >> 2)