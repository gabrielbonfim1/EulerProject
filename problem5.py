import math

def all_primes(x):
    global all_primos
    for i in x:
        if i not in primos:
            return False

    return True

nums = list(range(2,21))
primos= [2, 3, 5, 7, 11, 13, 17, 19]
#primos = [2,3,5,7]
init = 2

while all_primes(nums) == False:
    for primo in primos:
        mult = False
        for t in range(len(nums)):
            if nums[t]%primo == 0:
                nums[t]=nums[t]/primo
                print(nums, init)
                mult = True

        if mult:
            init = init * primo

print(init)