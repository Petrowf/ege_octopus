'''
На числовой прямой даны два отрезка: P  =  [69; 91] и Q  =  [77; 114]. Укажите наименьшую возможную длину такого отрезка A, для которого формула

(x ∈ Q) → (((x ∈ P) ≡ (x ∈ Q)) ∨ (¬(x ∈ P) → (x ∈ A)))

тождественно истинна (то есть принимает значение 1 при любом значении переменной х).
'''

P = range(69, 92)
Q = range(77, 115)
A_lens = []
for a1 in range(0, 200):
    for a2 in range(2, 202):
        A = range(a1, a2)
        flag = True
        for x in range(200):
            f = (x in Q) <= (((x in P) == (x in Q)) or (x not in P) <= (x in A))
            if f == False:
                flag = False
        if flag == True:
            A_lens.append(a2-a1)
print(min(A_lens))