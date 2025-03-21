with open("24var12.txt", encoding='utf-8') as file:
    text = file.read()

combs = text.split('AB')
cnt_max = 0
for i in range(len(combs) - 21):
    comb = combs[i:i+22]
    comb = ''.join(comb)
    cnt_max = max(cnt_max, len(comb) + 21*2)
print(cnt_max+2)