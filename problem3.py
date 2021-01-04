n = 600851475143
num = n
factors = []
primes =[]

i=2

while num>1:
    lret = True
    for t in primes:
        if i%t == 0:
            lret = False
            break
    if lret:
        primes.append(i)
        while num%i == 0:
            num = num/i
            if i not in factors:
                factors.append(i)

    i+=1

print(factors)
print(primes)