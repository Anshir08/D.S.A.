# My approach
# def bin(n):
#     l = []
#     while n:
#         l.append(str(n & 1))
#         n>>=1
#     return (''.join(l[::-1]))

# n = 12
# print("Binary representation of given number is",bin(12))

# # Iterative approach
# def bin(n) :
     
#     i = 1 << 31
#     while(i > 0) :
     
#         if((n & i) != 0) :
         
#             print("1", end = "")
         
#         else :
#             print("0", end = "")
             
#         i >>= 1
             
# bin(7)
# print()
# bin(4)

# Recursive approach
# def bin(n):
 
#     if n > 1:
#         bin(n//2)
 
#     print(n % 2, end="")
 
 
# # Driver Code
# if __name__ == "__main__":
 
#     bin(7)
#     print()
#     bin(4)


# InBuilt approach

def binary(num):
    return int(bin(num).split('0b')[1])
 
if __name__ == "__main__" :
    x = 10
    binary_x = binary(x)
    print(binary_x)