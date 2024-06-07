def isequation3(e1, e2):
    flag = True
    for P in range(2):
        for Q in range(2):
            for R in range(2):
                if(eval(e1) != eval(e2)):
                    flag = False
                    break
    return flag
e1 = '(not (P and Q)) or R '
e2 = '(not P) or ((not Q) or R)'
print(isequation3(e1, e2))