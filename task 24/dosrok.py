with open("24_dosrok.txt") as file:
    text = file.read()

abc12 = '0123456789AB'
chet = '02468A'
max_sub = ''
cur_sub = ''
last_chet = 0
i = 0
for ch in text:
    if ch in abc12:
        cur_sub += ch
        if ch in chet:
            last_chet = i
        i += 1
    else:
        cur_sub = cur_sub[:last_chet+1]
        cur_sub = cur_sub.lstrip('0')
        if len(cur_sub) > len(max_sub):
            max_sub = cur_sub
        i = 0
        last_chet = 0
        cur_sub = ''

cur_sub = cur_sub[:last_chet+1]
cur_sub = cur_sub.lstrip('0')
if len(cur_sub) > len(max_sub):
    max_sub = cur_sub

print(len(max_sub))

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

for num in text.split():
    num =  num.lstrip('0')
    if len(num) > 0:
        while num[-1] not in '02':
            num = num[0: len(num)-1]
            if len(num) == 0:
                break
            #print(num)
        cnt = max(cnt, len(num))

print(cnt)