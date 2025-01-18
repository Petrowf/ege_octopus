with open("24.txt", encoding='utf-8') as file:
    bad_words = 'ABCD-*'
    text = file.read()
    text = text.split("A")
    results = []
    stroka = ''

    for strok in text:

        if len(strok) != 0:
            if strok[0] != '+':
                for char in strok:
                    if char not in bad_words:
                        stroka += char
                    else:
                        while stroka.endswith('+'):
                            stroka = stroka[:-1]
                        results.append(eval(stroka))
                        break

print(max(results))