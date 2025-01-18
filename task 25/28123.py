for i in range(125256, 125331):
    d=[]
    for j in range(1, int(i**0.5)+1):
        if i%j==0:
            if j%2==0:
                d.append(j)
            if (i//j)%2==0:
                d.append(i//j)
    d = set(d)
    if len(d)==6:
        print(sorted(d))

