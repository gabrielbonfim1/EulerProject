n = 100
sum_square = 0

for i in range(1,n+1):
    sum_square = sum_square + i**2

square_sum = sum(range(1,n+1))**2

print(square_sum-sum_square)