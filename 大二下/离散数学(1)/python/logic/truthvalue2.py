def print01(truthtable):
    for tv in truthtable:
        if(tv):
            print ("1",end = "  ")
        else:
            print ("0",end = "  ")
    print("")
    return
                        
def printtf(truthtable):
    for tv in truthtable:
        print ("%r"%tv,end = "  ")
    print("")
    return

def commutativelaw3(p,q):
    f0=p ^ q
    f1=q ^ p
    return (f0,f1)

def truthtable2( ):
    truth={True,False}
    print("p q  f0 f1 f2")
    for p in truth:
        for q in truth:
            (f0,f1)=commutativelaw3(p,q)
            f2=(f0 == f1)
            print01((p,q,f0,f1,f2))
    return

def truthtable3( ):
    print("p  q  r  f0  f1 f2")
    truth={True,False}
    for p in truth:
        for q in truth:
            for r in truth:
                (f0,f1)=distributivelaw1(p,q,r)
                f2= (f0 == f1)
                print01((p,q,r,f0,f1, f2))
    return

def main( ):
    truthtable2( )
    return
                                                
