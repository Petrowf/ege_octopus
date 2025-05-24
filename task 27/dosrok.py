def d(point1, point2):
    dist = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    return dist

claster1 = []
claster2 = []
with open("dosrok_A.txt") as file:
    for row in file.readlines():
        row = row.replace(',', '.')
        x, y =  map(float, row.split())
        if y < 0:
            claster1.append((x, y))
        else:
            claster2.append((x, y))

min_sum = 1000000
centre1 = (0, 0)
for point1 in claster1:
    sum_dist = 0
    for point2 in claster1:
        sum_dist += d(point1, point2)
    if sum_dist < min_sum:
        min_sum = sum_dist
        centre1 = point1

min_sum = 1000000
centre2 = (0, 0)
for point1 in claster2:
    sum_dist = 0
    for point2 in claster2:
        sum_dist += d(point1, point2)
    if sum_dist < min_sum:
        min_sum = sum_dist
        centre2 = point1

print(int((centre1[0] + centre2[0])*5000), int((centre1[1] + centre2[1])*5000))

claster1 = []
claster2 = []
claster3 = []
with open("dosrok_B.txt") as file:
    for row in file.readlines():
        row = row.replace(',', '.')
        x, y =  map(float, row.split())
        if x < 0:
            claster1.append((x, y))
        elif y > 0:
            claster2.append((x, y))
        else:
            claster3.append((x, y))

min_sum = 1000000
centre1 = (0, 0)
for point1 in claster1:
    sum_dist = 0
    for point2 in claster1:
        sum_dist += d(point1, point2)
    if sum_dist < min_sum:
        min_sum = sum_dist
        centre1 = point1

min_sum = 1000000
centre2 = (0, 0)
for point1 in claster2:
    sum_dist = 0
    for point2 in claster2:
        sum_dist += d(point1, point2)
    if sum_dist < min_sum:
        min_sum = sum_dist
        centre2 = point1

min_sum = 1000000
centre3 = (0, 0)
for point1 in claster3:
    sum_dist = 0
    for point2 in claster3:
        sum_dist += d(point1, point2)
    if sum_dist < min_sum:
        min_sum = sum_dist
        centre3 = point1

print(int(((centre1[0] + centre2[0] + centre3[0])/3)*10000), int(((centre1[1] + centre2[1] + centre3[1])/3)*10000))