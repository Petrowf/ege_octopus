with open("24var12.txt", encoding='utf-8') as file:
    text = file.read()

max_len = 0

text = text.replace('AB', 'A B')
text = text.split(' ')
for i in range(0, len(text) - 22):
    sub = text[i: i + 22]
    sub = ''.join(sub)
    max_len = max(len(sub), max_len)

print(max_len)