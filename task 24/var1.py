with open('24var01.txt', encoding='utf-8') as file:
    text = '-' + file.read()

text = text.replace('+', '-')
text = text.replace('--', '- -')
for n in '234':
    text = text.replace(n, '1')
while '-00' in text:
    text = text.replace('-00', '-0 -0')

text = text.replace('-01', '-0 1')
max_len = 0
for sub in text.split():
    max_len = max(max_len, len(sub.strip('-')))
print(max_len)


