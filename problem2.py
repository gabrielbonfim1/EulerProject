fibo = [1,2]

while fibo[-1] <= 4000000:
    fibo.append(fibo[-1]+fibo[-2])

print(fibo)

sum = 0
for i in fibo:
    if i%2 == 0:
        sum += i

print(sum)