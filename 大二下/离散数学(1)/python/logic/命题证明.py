def print01(truthtable):
    for tv in truthtable:
        if(tv):
            print ("1",end = "  ")
        else:
            print ("0",end = "  ")
    print("")
    return

def proposition1(p,q,r):
    f0=((not p) | ((not q) | r))
    f1=((not  q) | ((not p) | r))
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition2(p,q,r):
    f0=((not q) | r)
    f1=(not (not  p | q)) | ((not p) | r)
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition3(p,q,r):
    f0=((not  p) | q)
    f1=(not (not  q | r)) | ((not p) | r)
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition4(q):
    f0=q
    f1=q
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition5(q):
    f0=(not (not q))
    f1=q
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition6(q):
    f0=q
    f1=(not (not q))
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition7(q,r):
    f0=(not(not(not  q))) | (not(not r))
    f1=(not q) | r
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition8(q,r):
    f0=(not q) | r
    f1=(not(not(not  q))) | (not(not r))
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition9(q,r):
    f0=(not q) | r
    f1=(not(not r)) | (not q)
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition10(q,r):
    f0=(not (not q)) | r
    f1=(not(not r)) | q
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition11(q,r):
    f0=(not q) | (not r)
    f1=(not r) | (not q)
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition12(q,r):
    f0=(not q)
    f1=(not q) | r
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition13(q):
    f0=(not (not q)) |q
    f1=q
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition14(q,r):
    f0=(not (not q)) |q
    f1=(not r) | q
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def proposition15(q,r):
    f0=q
    f1=(not(not q) | r) |r
    f2=((not f0) | f1)
    return  (f0,f1,f2)

def truthtable1( ):
    truth={True,False}
    print("q  f0 f1 f2")
    for q in truth:
        (f0,f1,f2)=proposition13(q)
        print01((q,f0,f1,f2))
    return

def truthtable2( ):
    truth={True,False}
    print("p q  f0 f1 f2")
    for q in truth:
        for r in truth:
            (f0,f1,f2)=proposition15(q,r)
            print01((q,r,f0,f1,f2))
    return

def truthtable3( ):
    print("p  q  r  f0  f1 f2")
    truth={True,False}
    for p in truth:
        for q in truth:
            for r in truth:
                (f0,f1,f2)=proposition3(p,q,r)
                print01((p,q,r,f0,f1, f2))
    return

def main( ):
    truthtable3( )
    return
