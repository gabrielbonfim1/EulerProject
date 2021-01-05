from funcoes import is_pandigital
from funcoes import is_prime
from funcoes import gen_primes
import itertools

pandigtals10 = [''.join(p) for p in itertools.permutations('1234567',7)]
print(len(pandigtals10))
pandigtals10=set(pandigtals10)
print(len(pandigtals10))
max=0
for i in pandigtals10:
    if is_prime(int(i)) and int(i)>max:
        max=int(i)

print(max)
