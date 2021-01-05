import itertools
def gen_pentagonal(n):
    pen = []
    for i in range(1,n+1):
        pen.append(int(i*(3*i-1)/2))
    return(pen)

def pen_test(x):
    if (((24*x+1)**(0.5)+1)/6).is_integer():
        return True
    else:
        return False


num = 100000
pentagonal = gen_pentagonal(num)
print(pentagonal)

combs = list(itertools.combinations(pentagonal,2))
#print(combs)
D = 100000000000
for i in combs:
    if pen_test(i[0]+i[1]) and pen_test(abs(i[0]-i[1])) and abs(i[0]-i[1])<D:
        D = abs(i[0]-i[1])
print(D)
