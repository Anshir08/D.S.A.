def reverseDigits(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num //= 10

    return rev

def square(num):
    return (num * num)

def checkAdamNumber(num):

    # r = int(str(num)[::-1])
     
    # a = int(str(num*num))
    # b = int(str(r*r)[::-1])
    a = square(num)
    b = square(reverseDigits(num))
    
    if a == reverseDigits(b):
        return True
    return False


num = 13
if checkAdamNumber(num):
    print("Adam Number")
else:
    print("Not a Adam Number")