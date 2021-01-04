res=[]
for i in range(10000000):
    string = str(i)
    som=0
    for digito in string:
        som = som + int(digito)**5
    if som==i:
        res.append(i)

print(sum(res)-1)