d = 256

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    p = 0
    t = 0
    h = 1

    for i in range(M-1):
        h = (h*d)%q

    for i in range(M):
        p = (p*d + ord(pat[i]))%q
        t = (t*d + ord(txt[i]))%q 

    for i in range(N-M+1):

        if p==t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j+=1 
                    
                if j==M:
                    print("Pattern found at index ",i)
        
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

        if t < 0:
            t = t+q

# Driver's Code
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
 
q = 101
 
search(pat,txt,q)