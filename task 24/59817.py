with open(r"C:\Users\petrowf\Downloads\24 (1).txt", encoding='utf-8') as file:
    stroka = file.read()
    sep = ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
    for s in sep:
        stroka = stroka.replace(s, s[0] + ' ' + s[1])
    len_stroks = list(map(len, stroka.split()))
    print(max(len_stroks))