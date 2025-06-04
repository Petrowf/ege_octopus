i = 1
cnt = 0
for ch1 in 'АГЕИЛНРТ':
    for ch2 in 'АГЕИЛНРТ':
        for ch3 in 'АГЕИЛНРТ':
            for ch4 in 'АГЕИЛНРТ':
                for ch5 in 'АГЕИЛНРТ':
                    slovo = ch1 + ch2 + ch3 + ch4 + ch5
                    if (i%2 == 1) and (slovo[0] != 'Т') and (slovo.count('Н') == 1 or slovo.count('Н') == 2):
                        cnt += 1
                    i += 1

print(cnt)
