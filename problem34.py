import math
resp=0
for i in range(3,100000):
    sum=0
    for t in str(i):
        sum = sum + math.factorial(int(t))

    if sum==i:
        resp = resp + i

print(resp)