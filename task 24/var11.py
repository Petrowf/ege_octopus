with open("24var11.txt") as file:
    text = file.read()
max_len = 0
textmax = text.replace('AB', 'A B')

textmax = textmax.split()
for i in range(len(textmax)-23):
    sub = ''.join(textmax[i:i+23])
    max_len = max(max_len, len(sub))

textmin = text.replace('AB', ' ')
textmin = textmin.split()
min_len = 10000000
for i in range(1, len(textmin) - 19):
    sub = ''.join(textmin[i:i+19])
    min_len = min(min_len, len(sub) + 2*21)

print(min_len, max_len)