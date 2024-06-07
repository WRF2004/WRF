e1 = 'P or (Q and R)'
e2 = '(P or R) and (P or Q)'
print('P', 'Q', 'R', e1, e2)
for P in range(2):
    for Q in range(2):
        for R in range(2):
            print(P, Q, R, int(eval(e1)), int(eval(e2)), int(eval(e1) == eval(e2)))
