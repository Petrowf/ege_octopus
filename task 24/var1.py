with open('24var01.txt', encoding='utf-8') as file:
    text = file.read()

# import sys
# sys.setrecursionlimit(100000)

bad_words = ['--', '-+', '+-', '++']
for bw in bad_words:
    text = text.replace(bw, 'W')
a = text.split('W')
max_len = 0
numbers = '0123456789'
for i in a:
    cur = ''
    for j in range(len(i)-1):
        cur += i[j]
        if i[j] == '0' and (i[j+1] in numbers):
            len_cur = len(cur)
            if len(cur) != 0:
                if cur[0] == '-' or cur[0] == '+':
                    len_cur -= 1
                if cur[-1] == '-' or cur[-1] == '+':
                    len_cur -= 1
            max_len = (len_cur, max_len)
            cur = ''

print(max_len)


