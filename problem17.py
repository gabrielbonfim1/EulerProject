from num2words import num2words as n2

n=1000
sum=0
for i in range(1,n+1):
    word=n2(i)
    word=word.replace(' ','')
    word=word.replace('-','')
    sum = sum + len(word)

print(sum)