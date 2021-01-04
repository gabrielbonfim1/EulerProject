def is_triplet(a,b,c):
    if (a**2 + b**2)==c**2:
        return True
    else:
        return False

triplets=[]
for a in range(1,999):
    for b in range(a,998):
        c = 1000 - a - b
        if is_triplet(a,b,c):
            print(a*b*c)
            exit


