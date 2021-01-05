def r(S,index):
    S = S[:index] + S[index + 1:]
    return S


max_value = 99
pares=[]
num=''
den=''

for denominador in range(11,max_value+1):
    for numerador in range(10,denominador):
        for i in range(2):
            for j in range(2):
                if str(numerador)[i]==str(denominador)[j] and str(denominador)[1]!=0:
                    num = r(str(numerador),i)
                    den = r(str(denominador),j)
                    if float(den)!=0:
                        if float(num)/float(den) == numerador/denominador:
                            if numerador%10==0 and denominador%10==0:
                                continue
                            else:
                                pares.append(f"{numerador}/{denominador}")
print(pares)
#numerador do produto = 387296
#denominador do produto = 38729600