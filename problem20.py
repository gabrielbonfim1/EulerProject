import math

fat = str(math.factorial(100))

sum=0
for i in fat:
    sum = sum + int(i)

print(sum)