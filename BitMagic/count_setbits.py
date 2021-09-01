# BUILT_in_Func

# print(bin(4).count('1'));
# print(bin(15).count('1'));



# Recursive approach for BK's algo

# def countSetBits(n):
 
#     # base case
#     if (n == 0):
#         return 0
#     else:
#         return 1 + countSetBits(n & (n - 1)) # Brian Kernighan’s Algorithm
             
# n = 9
# print(countSetBits(n))




# Using lookup table---

# BitsSetTable256 = [0] * 256
 
# # Function to initialise the lookup table
# def initialize():
     
#     # To initially generate the
#     # table algorithmically
#     BitsSetTable256[0] = 0
#     for i in range(256):
#         BitsSetTable256[i] = (i & 1) + BitsSetTable256[i // 2]
 
# # Function to return the count
# # of set bits in n
# def countSetBits(n):
#     return (BitsSetTable256[n & 0xff] +
#             BitsSetTable256[(n >> 8) & 0xff] +
#             BitsSetTable256[(n >> 16) & 0xff] +
#             BitsSetTable256[n >> 24])
 
# # Driver code
 
# # Initialise the lookup table
# initialize()
# n = 9
# print(countSetBits(n))



# Mapping numbers with the bit
# (Recursive approach for lookup table method)

num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

def CountSetBitsRec(num):
    nibble = 0
    if num == 0:
        return num_to_bits[0]

    nibble = num & 0xf

    return num_to_bits[nibble] + CountSetBitsRec(num >> 4)

# Driver's Code

num = 9
print(CountSetBitsRec(num))