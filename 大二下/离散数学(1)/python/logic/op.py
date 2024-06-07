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

def logicalop( ):
  truth={True,False}
  print("p  q  f0")
  for p in truth:
    for q in truth:
      f0= p & q
      print01((p,q,f0))
  return

def logicaloplaw2( ):
  truth={True,False}
  tv=True
  for Q in truth:
    for R in truth:
      E1=Q&R
      E2=R&Q
      tv=tv&(E1==E2)
  return tv

def logicaloplaw3( ):
  truth={True,False}
  tv=True
  for P in truth:
    for Q in truth:
      for R in truth:
        E1=P&(Q|R)
        E2=P&Q|P&R
        tv=tv&(E1==E2)
  return tv

def assignmentfunction(sigma):
  Q=sigma[0]
  R=sigma[1]
  tv=(not(not(Q&R)))|((not Q)|(not R))
  return tv

def truthvalue( ):
  print("p  q  f0 f1 f2 f3 f4 f5")
  truth={True,False}
  tv=True
  for q in truth:
    for r in truth:
      f0=q&r
      f1=(not f0)
      f2=(not q)
      f3=(not r)
      f4=f2|f3
      f5=((not f1)|f4)&((not f4) | f1)
      print01((q,r,f0,f1,f2,f3,f4,f5))
  return

def main():
  truthvalue( )
  return
