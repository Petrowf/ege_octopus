with open("dosrok.txt", encoding='utf-8') as file:
    text = file.read()

cnt = 0
abc = "0123456789AB"
not_abc = "CDEFGHIJKLMNOPQRSTUVWXYZ"
for char in not_abc:
    text = text.replace(char, ' ')

for char in "13579B":
    text = text.replace(char, '1')

for char in "2468A":
    text = text.replace(char, '2')

while ' 0' in text:
    text = text.replace(' 0', ' ')

for num in text.split():
    while (num[-1] != '0' and num[-1] != '2'):
        num = num[0: len(num)-1]
        if len(num) == 0:
            break
        #print(num)
    cnt = max(cnt, len(num))

print(cnt)
