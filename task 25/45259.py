for i in range(10):
    for j in range(10):
        a=int('12345' + str(i) + '7' + str(j) + '8')
        if a%23==0:
            c=a//23
            print(a,c)