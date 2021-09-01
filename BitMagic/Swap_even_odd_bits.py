def swapBits(x):

    # even_bits = x & 0xAAAAAAAA

    # odd_bits = x & 0x55555555

    # even_bits >>= 1

    # odd_bits <<= 1

    # return (even_bits | odd_bits)

    return (((x & 0xAAAAAAAA)>>1) | ((x & 0x55555555)<<1))

# Driver's program
# 00010111
x = 23 

# Output is 43 (00101011)
print(swapBits(x))