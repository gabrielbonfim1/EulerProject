import itertools

pares = list(itertools.product(range(2,101),repeat=2))

nums = []

for t in pares:
    nums.append(t[0]**t[1])

nums.sort()

nums = list(dict.fromkeys(nums))
print(len(nums))