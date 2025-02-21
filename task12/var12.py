stroka = '22' + '1'*2023

while '2111'in stroka or '1112'in stroka:
    stroka = stroka.replace('111', '1', 1)
    if '21' in stroka:
        stroka = stroka.replace('21', '12', 1)
    else:
        stroka = stroka.replace('12', '1', 1)

print(stroka)