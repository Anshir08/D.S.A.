IntBits = 32

def leftRotate(n, d):
    
    return n << d | n >> (IntBits - d)

def rightRotate(n, d):
    
    return (n >> d) | (n << (IntBits - d)) & 0xFFFFFFFF



if __name__ == '__main__':
    n = 16
    d = 2
    
    print("Left Rotation of",n,"by"
        ,d,"is",end=" ")
    print(leftRotate(n, d))
    
    print("Right Rotation of",n,"by"
        ,d,"is",end=" ")
    print(rightRotate(n, d))