import logic as ll
S = '(not (Q and ((not Q) or R))) or R'
print('Q', 'R', S)
for Q in range(2):
    for R in range(2):
        print(Q, R, int(eval(S)))