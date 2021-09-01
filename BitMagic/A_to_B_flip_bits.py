# def countSetBits( n ):
#     count = 0
#     while n:
#         count += 1
#         n &= (n-1)
#     return count


def FlippedCount(a, b):

  #  return countSetBits(a^b) 

     return bin(a^b).count('1')


a = 10
b = 20
print(FlippedCount(a, b))