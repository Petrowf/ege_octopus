with open(r"C:\Users\petrowf\Downloads\09.txt", encoding='utf-16') as file:
    cnt = 0
    for row in file:
        numbers = list(map(int, row.split()))
        # максимальное число встречается в строке ровно один раз
        if numbers.count(max(numbers)) == 1:
            first = 1
        else:
            first = 0

        # хотя бы одно число в строке повторяется более одного раза
        second = 0
        for n in numbers:
            if numbers.count(n) > 1:
                second = 1

        # аксимальное число в строке превышает среднее арифметическое всех остальных чисел этой строки более чем в три раза
        #wthout_max = [i for i in numbers if i != max(numbers)]
        without_max = []
        for n in numbers:
            if n != max(numbers):
                without_max.append(n)
        third = 0
        sr_ar= sum(without_max) / len(without_max)
        if max(numbers) / sr_ar > 3:
            third = 1

        cnt += first*second*third

print(cnt)