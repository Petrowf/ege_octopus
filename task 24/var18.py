with open("24var17-20.txt", encoding='utf-8') as file:
    text = file.read()

while 'XY' in text:
    text = text.replace('XY', 'X Y')

while 'YZ' in text:
    text = text.replace('YZ', 'Y Z')

while 'XZ' in text:
    text = text.replace('XZ', 'X Z')
cnt = 0
for sub in text.split():
    cnt = max(cnt, len(sub))

print(cnt)