def magicNumber(n):
    pow = 1
    answer = 0

    while(n):
        pow = pow*5

        if n & 1:
            answer += pow

        n >>= 1 # or n = n/2

    return answer

n = 5
print("nth magic number is", magicNumber(n))