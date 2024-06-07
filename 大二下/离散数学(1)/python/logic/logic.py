def print01(truthtable):
    for tv in truthtable:
        if(tv):
            print ("1",end = "  ")
        else:
            print ("0",end = "  ")
    print("")
    return

def truthtable2(s):
    w='Q  R  '+s
    print("%r"%w)
    truth={True,False}
    for Q in truth:
        for R in truth:
            f=eval(s)
            t=[Q,R]+[f]
            print01(t)
    return

def truthtable3(s):
    w='P  Q  R  '+s
    print("%r"%w)
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f=eval(s)
                t=[P,Q,R]+[f]
                print01(t)
    return

def isequation20(q,r,e1,e2):
    w=q+'  '+r+'  '+e1+'  '+e2+'  e1==e2'
    print("%r"%w)
    e1=e1.replace(q,'Q')
    e1=e1.replace(r,'R')
    e2=e2.replace(q,'Q')
    e2=e2.replace(r,'R')
    truth={True,False}
    for Q in truth:
        for R in truth:
            f1=eval(e1)
            f2=eval(e2)
            t=[Q,R]+[f1,f2]+[f1==f2]
            print01(t)
    return

def isequation30(p,q,r,e1,e2):
    w=p+'  '+q+'  '+r+'  '+e1+'  '+e2+'  e1==e2'
    print("%r"%w)
    e1=e1.replace(p,'P')
    e1=e1.replace(q,'Q')
    e1=e1.replace(r,'R')
    e2=e2.replace(p,'P')
    e2=e2.replace(q,'Q')
    e2=e2.replace(r,'R')
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f1=eval(e1)
                f2=eval(e2)
                t=[P,Q,R]+[f1,f2]+[f1==f2]
                print01(t)
    return

def isargument2(pre,s):
    w='Q R '
    for u in pre:
        w=w+u+' '
    w=w+'╞'+s
    print(w)
    truth={True,False}
    for Q in truth:
        for R in truth:
            pv=[]
            for pk in pre:
                pv=pv+[eval(pk)]
            f=eval(s)
            t=[Q,R]+pv+[f]
            print01(t)
    return

def isargument3(pre,s):
    w='P Q R '
    for u in pre:
        w=w+u+' '
    w=w+'╞'+s
    print(w)
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                pv=[]
                for pk in pre:
                    pv=pv+[eval(pk)]
                f=eval(s)
                t=[P,Q,R]+pv+[f]
                print01(t)
    return

def isargument4(pre,s):
    w='P Q R S '
    for u in pre:
        w=w+u+' '
    w=w+'╞'+s
    print(w)
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                for S in truth:
                    pv=[]
                    for pk in pre:
                        pv=pv+[eval(pk)]
                    f=eval(s)
                    t=[P,Q,R,S]+pv+[f]
                    print01(t)
    return

def isequation1(e1,e2):
    w='Q  '+e1+'  '+e2+'  e1==e2'
    print(w)
    truth={True,False}
    for Q in truth:
        f1=eval(e1)
        f2=eval(e2)
        t=[Q]+[f1,f2]+[f1==f2]
        print01(t)
    return

def isequation2(e1,e2):
    w='Q  R  '+e1+'  '+e2+'  e1==e2'
    print(w)
    truth={True,False}
    for Q in truth:
        for R in truth:
            f1=eval(e1)
            f2=eval(e2)
            t=[Q,R]+[f1,f2]+[f1==f2]
            print01(t)
    return

def isequation3(e1,e2):
    w='P  Q  R  '+e1+'  '+e2+'  e1==e2'
    print(w)
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f1=eval(e1)
                f2=eval(e2)
                t=[P,Q,R]+[f1,f2]+[f1==f2]
                print01(t)
    return

def isargument20(q,r,pre,s):
    w=q+'  '+r+'  '
    for u in pre:
        w=w+u+'  '
    w=w+s
    s=s.replace(q,'Q')
    s=s.replace(r,'R')
    ps=[]
    for pk in pre:
        pk=pk.replace(q,'Q')
        pk=pk.replace(r,'R')
        ps=ps+[pk]
    print("%r"%w)
    truth={True,False}
    for Q in truth:
        for R in truth:
            pv=[]
            for pk in ps:
                pv=pv+[eval(pk)]
            f=eval(s)
            t=[Q,R]+pv+[f]
            print01(t)
    return

def isargument30(p,q,r,pre,s):
    w=p+'  '+q+'  '+r+'  '
    for u in pre:
        w=w+u+'  '
    w=w+s
    print("%r"%w)
    s=s.replace(p,'P')
    s=s.replace(q,'Q')
    s=s.replace(r,'R')
    ps=[]
    for pk in pre:
        pk=pk.replace(p,'P')
        pk=pk.replace(q,'Q')
        pk=pk.replace(r,'R')
        ps=ps+[pk]
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                pv=[]
                for pk in ps:
                    pv=pv+[eval(pk)]
                f=eval(s)
                t=[P,Q,R]+pv+[f]
                print01(t)
    return

def issubstitution2(s,t,s1):
    w='Q  R '+'f1'+' '+'f2'+'  f1==f2'
    print("%r"%w)
    rv=[s,t,s1]
    truth={True,False}
    for Q in truth:
        for R in truth:
            f1=eval(s.replace(t,s1))
            v=str(eval(s1))
            f2=eval(s.replace(t,v))
            tv=[Q,R]+[f1,f2]+[f1==f2]
            print01(tv)
    return

def issubstitution3(p,q,r,s,t,s1):
    w='P  Q  R '+'f1'+' '+'f2'+'  f1==f2'
    print("%r"%w)
    rv=[s,t,s1]
    truth={True,False}
    for P in truth:
        for Q in truth:
            for R in truth:
                f1=eval(s.replace(t,s1))
                v=str(eval(s1))
                f2=eval(s.replace(t,v))
                tv=[P,Q,R]+[f1,f2]
                print01(tv)
    return rv

def issubstitution20(q,r,s,t,s1):
    w=q+'  '+r+' '+'f1'+' '+'f2'+'  f1==f2'
    print("%r"%w)
    rv=[s,t,s1]
    truth={True,False}
    s=s.replace(q,'Q')
    s=s.replace(r,'R')
    t=t.replace(q,'Q')
    t=t.replace(r,'R')
    s1=s1.replace(q,'Q')
    s1=s1.replace(r,'R')
    for Q in truth:
        for R in truth:
            f1=eval(s.replace(t,s1))
            v=str(eval(s1))
            f2=eval(s.replace(t,v))
            tv=[Q,R]+[f1,f2]+[f1==f2]
            print01(tv)
    return

def issubstitution30(p,q,r,s,t,s1):
    w=p+'  '+q+'  '+r+' '+'f1'+' '+'f2'
    print("%r"%w)
    rv=[s,t,s1]
    truth={True,False}
    s=s.replace(p,'P')
    s=s.replace(q,'Q')
    s=s.replace(r,'R')
    t=t.replace(p,'P')
    t=t.replace(q,'Q')
    t=t.replace(r,'R')
    s1=s1.replace(p,'P')
    s1=s1.replace(q,'Q')
    s1=s1.replace(r,'R')
    for P in truth:
        for Q in truth:
            for R in truth:
                f1=eval(s.replace(t,s1))
                v=str(eval(s1))
                f2=eval(s.replace(t,v))
                tv=[P,Q,R]+[f1,f2]
                print01(tv)
    return rv

def dualformula(s):
    s1=s.replace('∨','|')
    s1=s1.replace('∧','∨')
    s1=s1.replace('|','∧')
    s1=s1.replace('0','F')
    s1=s1.replace('1','0')
    s1=s1.replace('F','1')
    return s1

def invassignment(s):
    s = s.replace('P', '(¬P)')
    s = s.replace('Q', '(¬Q)')
    s = s.replace('R', '(¬R)')
    return s

def dualraplace(s):
    s=s.replace('∨','|')
    s=s.replace('∧','&')
    s=s.replace('¬','not ')
    return s

def dualformula1(s0):
    s1=s0.replace('∨','|')
    s1=s1.replace('∧','∨')
    s1=s1.replace('|','∧')
    s1=s1.replace('0','F')
    s1=s1.replace('1','0')
    s1=s1.replace('F','1')
    e0=s0.replace('∨','|')
    e0=e0.replace('∧','&')
    e0=e0.replace('¬','not ')
    e1=s1.replace('∨','|')
    e1=e1.replace('∧','&')
    e1=e1.replace('¬','not ')
    return [s1,e0,e1]

