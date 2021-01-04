primes = [2]
i=3
while len(primes)<10001:
    prim = True
    for t in primes:
        if i%t == 0:
            prim = False
            break

    if prim:
        primes.append(i)
    i+=1
print(max(primes))