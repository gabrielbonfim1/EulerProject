lado = 1001
n = lado**2

i=1
sum=1
t=2
count=0
while i<=n:
   if (i-1)%t==0:
       sum=sum+i
       count+=1
       if count==4:
           t+=2
           count=0
   i+=1

print(sum-1)

