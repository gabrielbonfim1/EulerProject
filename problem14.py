n=1000000

start = 13
max=[13,10]

for start in range(1,n):
    sequence = [start]
    while sequence[-1]!=1:
        if sequence[-1]%2==0:
            sequence.append(int(sequence[-1]/2))
        else:
            sequence.append((int(sequence[-1]*3) +1))


    if len(sequence)>max[1]:
        max[0]=start
        max[1]=len(sequence)
        #print(start,sequence)

print(max)