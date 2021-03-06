import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):

    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

if __name__ == '__main__':
    for i in range(11):
        if isFibonacci(i):
            print(i,"is a Fibonacci Number")
        else:
            print(i, "is not a Fibonacci number")