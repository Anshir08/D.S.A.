def convert0to5rec(num):
    if num == 0:
        return 0
    
    digit = num % 10

    if digit == 0:
        digit = 5

    return convert0to5rec(num//10) *10 + digit 


def convert0to5(num):
    if num == 0:
        return 5
    else:
        return convert0to5rec(num)

# Driver's Program
num = 10120
print(convert0to5(num))