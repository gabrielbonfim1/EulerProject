fibbo = [1,1]

i=2
while len(str(fibbo[-1]))<1000:
    fibbo.append(fibbo[-1]+fibbo[-2])
    i+=1

print(fibbo)
print(i)
