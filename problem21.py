def d(x):
    sum = 0
    for i in range(1,x):
        if x%i==0:
            sum = sum + i

    return(sum)

amicable=[]

for a in range(1,10001):
    b = d(a)
    if d(b)==a and a!=b:
        amicable.append(a)

print(sum(amicable))