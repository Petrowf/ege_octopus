with open("24var11.txt") as file:
    text = file.read()
min_len = 100000000000000000
text = text.split('AB')

for i in range(len(text) - 20):
    sub = text[i:i+20]
    sub = ''.join(sub)
    min_len = min(len(sub) + 21*2, min_len)

print(min_len)