for n in range(100, 1000):
    sum1 = int(str(n)[0])**2 + int(str(n)[1])**2
    sum2 = int(str(n)[1])**2 + int(str(n)[2])**2
    result = str(max(sum1, sum2)) + str(min(sum1, sum2))
    if result == '9752':
        print(n)