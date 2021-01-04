import math

palis = []

def is_palindrome(x):
    x = str(x)
    if len(x)%2 ==0:
        i = int(len(x)/2)
        t = i+1
    else:
        i = t = int(math.ceil(len(x)/2))

    lret = True
    while i>0:
        if x[i-1]==x[t-1]:
            i-=1
            t+=1
        else:
            lret = False
            break

    return lret

for i in range(100,1000):
    for t in range(100,1000):
        if is_palindrome(i*t):
            palis.append(i*t)

print(max(palis))