from collections import Counter

def list_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def t_number(x):
    sum = 0
    for i in range(1,x+1):
        sum = sum + i
    return (sum)



def num_divisores(x):
    divs = []
    sum = 1
    global primes
    i=0
    while x>1:
        while x%primes[i]==0:
            x=x/primes[i]
            divs.append(primes[i])
        i+=1

    for i in Counter(divs).values():
        sum = sum*(i+1)
    return sum


primes = list_primes(100000)

counter = 1
k = t_number(counter)

while num_divisores(k)<500:
    counter+=1
    k=t_number(counter)

print(counter,k,num_divisores(k))

