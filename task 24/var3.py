with open("24var03.txt", encoding='utf-8') as file:
    text = file.read()

text = text.replace('*', '-')

while '--' in text:
    text = text.replace('--','- -')

for char in '123456789':
    text = text.replace(char, '1')

while '-00' in text:
    text = text.replace('-00', '-0 -0')
while '-01' in text:
    text = text.replace('-01', '-0 1')

#print(text)
cnt = 0

for num in text.split():
    num = num.strip('-')
    if len(num) == 599:
        print(num)
    cnt = max(cnt, len(num))

print(cnt)