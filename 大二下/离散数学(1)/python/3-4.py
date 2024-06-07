pre =['P', '(not Q) or ((not P) or R)']
post = '(not Q) or R'
print('P', 'Q', 'R', pre[0], pre[1], post)
for P in range(2):
    for Q in range(2):
        for R in range(2):
            print(P, Q, R, int(eval(pre[0])), int(eval(pre[1])), int(eval(post)))
