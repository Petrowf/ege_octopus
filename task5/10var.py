for n in range(100):

    #строим двоичную запись числа n
    n1 = n
    bin_n = ''
    while n1 != 0:
        bin_n = str(n1 % 2) + bin_n
        n1 = n1 // 2
    #после выполнения цикла в bin_n лежит двоичная запись
    #2 пункт
    if n % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'
    #3 пункт
    if bin_n.count('1') % 3 == 0:
        bin_n = '11' + bin_n[2:]
    else:
        bin_n = '10' + bin_n[2:]
    #Получаем R
    r = int(bin_n, base=2)
    if r <= 37:
        print(n)
