with open('24var01.txt', encoding='utf-8') as file:
    text = '+' + file.read()

max_len = 0

text = text.replace('-', '+')
text = text.replace('++', ' ')

nums = '1234'
for n in nums:
    text = text.replace(n, '1')

while '+00' in text:
    text = text.replace('+00','+0 +0')

text = text.replace('+01', '+0 1')

for sub in text.split():
    sub = sub.strip('+')
    max_len = max(len(sub), max_len)
    print(sub)

print(max_len)