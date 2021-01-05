import itertools
from funcoes import gen_primes

pandigtals10 = [''.join(p) for p in itertools.permutations('0123456789')]

primos = gen_primes(18)
sum=0
for t in pandigtals10:
    lret = True
    for i in range(7):
        num = int(t[i+1:i+4])
        if num%primos[i]!=0:
            lret=False
    if lret:
        sum = sum + int(t)

print(sum)

