with open('24var02.txt', encoding='utf-8') as file:
    text = '-' + file.read()
text = text.replace('+', '-')
text = text.replace('--', '- -')

for n in '678':
    text = text.replace(n, '5')

while '-00' in text:
    text = text.replace('-00', '-0 -0')

text = text.replace('-05', '-0 5')

max_len = 0
for sub in text.split():
    max_len = max(max_len, len(sub.strip('-')))

print(max_len)