with open(r"C:\Users\petrowf\Downloads\24.txt", encoding='utf-8') as file:
    stroka = file.read()
    min_len = 1000000000000000000
    podposls = stroka.split('W')[1:-1]
    for i in range(len(podposls)-129):
        podposl = ''.join(podposls[i:i+129])
        min_len = min(min_len, len(podposl) + 130)

print(min_len)