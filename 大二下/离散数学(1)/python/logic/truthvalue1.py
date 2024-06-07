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
    print ("%r"%tv)
  print(" ")
  return

def associativelaw1(p,q,r):
  f0=(p | q) | r
  f1=p | (q | r)
  return (f0,f1)

def associativelaw2(p,q,r):
  f0=(p & q) & r
  f1=p & (q & r)
  return (f0,f1)

def associativelaw3(p,q,r):
  f0=(p ^ q) ^ r
  f1=p ^ (q ^ r)
  return (f0,f1)

def associativelaw4(p,q,r):
  f0=(not ((not p) | q)) | r
  f1=(not p) | ((not q) | r)
  return (f0,f1)

def distributivelaw1(p,q,r):
  f0=p | (q & r)
  f1=(p | q) & (p | r)
  return (f0,f1)

def distributivelaw2(p,q,r):
  f0=p & (q | r)
  f1=(p & q) | (p & r)
  return (f0,f1)

def distributivelaw3(p,q,r):
  f0=p & (q ^ r)
  f1=(p & q) ^ (p & r)
  return (f0,f1)

def distributivelaw4(p,q,r):
  f0=(not p) | (q & r)
  f1=((not p) | q) & ((not p) | r)
  return (f0,f1)

def distributivelaw5(p,q,r):
  f0=(not p) | (q | r)
  f1=((not p) | q) | ((not p) | r)
  return (f0,f1)

def distributivelaw6(p,q,r):
  f0=(not p) | (q ^ r)
  f1=((not p) | q) ^ ((not p) | r)
  return (f0,f1)

def distributivelaw7(p,q,r):
  f0=p & ((not q) | r)
  f1=(not(p & q)) | (p & r)
  return (f0,f1)

def commutativelaw1(p,q):
  f0=p | q
  f1=q | p
  return (f0,f1)

def commutativelaw2(p,q):
  f0=p & q
  f1=q & p
  return (f0,f1)

def commutativelaw3(p,q):
  f0=p ^ q
  f1=q ^ p
  return (f0,f1)

def DeMorganlaw1(p,q):
  f0=not (p | q)
  f1=(not q) & (not p)
  return (f0,f1)

def DeMorganlaw2(p,q):
  f0=not (p & q)
  f1=(not q) | (not p)
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
        (f0,f1)=distributivelaw3(p,q,r)
        f2= (f0 == f1)
        print01((p,q,r,f0,f1, f2))
  return

def main( ):
  truthtable2( )
  return
                                                
