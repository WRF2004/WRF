def GodelCode(e):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','P','Q','R','S','x','y','c','├',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149]
    code=''
    for a in e:
        i=D.index(a)
        code=code+str(P[i])
    return code

def GodelCodes(E):
    codes=''
    for e in E:
        codes=codes+GodelCode(e)+'00'
    codes=codes+'22'
    return codes

def GodelDecodes(m):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','P','Q','R','S', 'x','y','c','├',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149]
    A=[]
    C=''
    k=0
    while m[k:k+2] != '22':
        if m[k:k+2] == '00':
            A=A+[C]
            C=''
            k=k+2
            continue
        if int(m[k]) in P:
            c=m[k]
            k=k+1
        elif int(m[k:k+2]) in P:
            c=m[k:k+2]
            k=k+2
        elif int(m[k:k+3]) in P:
            c=m[k:k+3]
            k=k+3
        i=P.index(int(c))
        C=C+D[i]
    return A

