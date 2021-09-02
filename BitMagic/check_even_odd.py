def isEven(n):

    return not (n&1)

if __name__ == '__main__':
    n = 101
    if isEven(n):
        print("Even")
    else:
        print("Odd")