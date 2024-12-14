with open(r"C:\Users\petrowf\Downloads\9.txt", encoding='utf-16') as file:
    c=0
    for i in file:
        s=list(map(int, i.split()))
        fir=0
        povt=[]
        nepovt=[]
        for k in s:
            if s.count(k)==2:
                povt.append(k)
            if s.count(k)==1:
                nepovt.append(k)
        if len(povt)==2 and len(nepovt)==4:
            fir=1
        second=0
        if len(nepovt)>0:
            sr=sum(nepovt)/len(nepovt)
            su=sum(povt)
            if sr<=su:
                second=1
        c+=fir*second
print(c)