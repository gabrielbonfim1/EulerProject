from funcoes import gen_primes

def num_prime_factors(x):
    primos = gen_primes(x+1)
    factors = []
    i=0
    while x > 1:
        if x%primos[i]==0:
            x = x/primos[i]
            if primos[i] not in factors:
                factors.append(primos[i])
        else:
            i+=1
    return len(factors)

lret=True
i=102380
while lret:
    #if num_prime_factors(i) == 3 and num_prime_factors(i + 1) == 3 and num_prime_factors(i + 2) == 3:
    if num_prime_factors(i)==4 and num_prime_factors(i+1)==4 and num_prime_factors(i+2)==4 and num_prime_factors(i+3)==4:
        lret = False
    else:
        i+=1
    print(i)





