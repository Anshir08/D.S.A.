st = []
 
def push_digits(number):
 
    while (number != 0):
        st.append(number % 10)
        number = int(number // 10)
 

def reverse_number(number):
     
    # Function call to push number's digits to stack

    push_digits(number)

    reverse = 0
    i = 1
    
    # Popping the digits 
    while (len(st) > 0):
        reverse = reverse + st[len(st)-1] * i
        st.pop()
        i *= 10

    return reverse
 
# Driver Code
number = 39997
print(reverse_number(number))