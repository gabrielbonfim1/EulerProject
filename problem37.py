from funcoes import is_prime
from funcoes import gen_primes

primes=gen_primes(4000000)
resp=[]
for i in primes:
    if len(str(i))==1:
        continue
    lret=True
    for t in range(len(str(i))):
        if len(str(i)[t:].replace(" ", ""))>0 and len(str(i)[0:-t].replace(" ", ""))>0:
            if not(is_prime(int(str(i)[t:])) and is_prime(int(str(i)[0:-t]))):
                lret=False
    if lret:
        resp.append(i)




print(resp)
print(f"Sum = {sum(resp)}")

