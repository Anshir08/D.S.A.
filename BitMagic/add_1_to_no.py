# Sol.1
def add1ToNumber(n):
    i = 1

    while n & i:
        n = n^i
        i <<= 1
    
    n = n^i
    return n

# Sol.2    
# using 2's complement
def addOne(n):

    return (-(~n))

# Driver's Code 
print(add1ToNumber(13))    
print(addOne(13))    