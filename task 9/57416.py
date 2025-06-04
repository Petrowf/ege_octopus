with open("57416.txt") as file:
    rows = file.readlines()
cnt = 0

for row in rows:
    row = list(map(int, row.split('\t')))
    if len(row) == len(set(row)):
        row.sort()
        max_n = row.pop(-1)
        min_n = row.pop(0)
        if 2*(max_n + min_n) <= sum(row):
            cnt += 1

print(cnt)