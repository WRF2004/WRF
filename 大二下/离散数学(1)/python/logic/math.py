import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import *
def cot(x):
    return cos(x)/sin(x)

def sec(x):
    return 1/cos(x)

global P
P=[]
global C
C=[]
global S
global LOGIC
LOGIC=1
global Ev
Ev=[]

def replacechar(s,x,y):
    if isinstance(s,str):
        c=s.replace(x,y)
        return c
    else:
        Ls=[]
        for a in s:
            Ls=Ls+[replacechar(a,x,y)]            
    return Ls

def isaxiom1schema(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    P=s[2][0]
    Q=s[0]
    p=[Q,'→',[P,'→',Q]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['axiom1',a]]

def isaxiom2schema(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[0][2]) != 3:
        return [False,a]
    P=s[0][0]
    Q=s[0][2][0]
    R=s[0][2][2]
    p=[[P,'→',[Q,'→',R]]]+['→']+[[[P,'→',Q],'→',[P,'→',R]]]
    tv=p == s
    a=[-1]
    if s in S:
        a=[S.index(s)]
    return [tv,['axiom2',a]]

def isaxiom3schema(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][2]
    R=s[2][0]
    p=[[['¬',Q],'→',['¬',R]]]+['→']+[[R,'→',Q]]
    tv=p == s
    a=[-1]
    if s in S:
        a=[S.index(s)]
    return [tv,['axiom3',a]]

def isaxiom4schema(s):
    tv=False
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    w=s[0][0]
    if len(w) != 2:
        return [False,a]
    if w[0] != '∀':
        return [False,a]
    Ax=s[0][0]
    x=w[1]
    y=s[2][1]
    if isinstance(y,list):
        y=y[1]
    elif isinstance(y,list):
        y=y[1]
    else:
        y=y
    Q0=s[0][1]
    tv=isinstance(x,str) and isinstance(y,str) and isinstance(Q0,list)
    if tv == False:
        return [False,a]     
    Q1=replacechar(Q0,x,y)
    p=[[Ax, Q0],'→',Q1]
    tv=(p==s)
    if s in S:
        a=[S.index(s)]
    return [tv,['axiom4',a]]

def isaxiom4schema2(s):
    tv=False
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    w=s[0][0]
    if len(w) != 2:
        return [False,a]
    if w[0] != '∀':
        return [False,a]
    Ax=s[0][0]
    Q=s[0][1]
    p=[[Ax, Q],'→',Q]
    tv=(p==s)
    if s in S:
        a=[S.index(s)]
    return [tv,['axiom4',a]]

def isaxiom5schema(s):
    tv=False
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    w=s[0][0]
    if len(w) != 2:
        return [False,a]
    if w[0] != '∀':
        return [False,a]
    if len(s[0][1]) != 3:
        return [False,a]
    w=s[0][1][0][0]
    Ax=s[0][0]
    Q=s[0][1][0]
    Qx=s[0][1][2]
    p=[[Ax,[Q,'→',Qx]],'→',[Q,'→',[Ax,Qx]]]
    tv=(p==s)
    if s in S:
        a=[S.index(s)]
    return [tv,['axiom5',a]]

def isMPschema(p):
    tv=False
    a=[-1,-1]
    for s in S:
        if len(s) == 3:
            if (s[2] == p) & (s[0] in S):
                i=S.index(s[0])
                j=S.index(s)
                k=S.index(p)
                if (i < k) and (j < k):
                    tv=True
                if s in S:
                    a=[S.index(s[0]),S.index(s)]
                break
    return [tv,['MP',a]]

def isUGchema(s):
    tv=False
    a=[-1]
    if len(s) != 2:
        return [False,a]
    w=s[0]
    if len(w) != 2:
        return [False,a]
    if w[0] != '∀':
        return [False,a]
    x=w[1]
    Q=s[1]
    p=['∀'+x, Q]
    tv=(p==s) and (Q in S)
    if (s in S) and (Q in S):
        a=[S.index(Q),S.index(s)]
    return [tv,['UG',a]]

def ispremise(s):
    a=[-1]
    tv=s in P
    if s in P:
        a=[P.index(s)]
    return [tv,['premise',a]]

def isconclusion(s):
    tv=s == C
    a=[S.index(s)]
    return [tv,a]

def isidentityschema(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    p=[Q,'→',Q]
    tv=p == s
    a=[-1]
    if s in S:
        a=[S.index(s)]
    return [tv,['(Q→Q)',a]]

def istransmissionschema(s):
    a=[-1]
    tv=False
    if len(s) != 3:
        return [False,a]
    P=s[0]
    R=s[2]
    for p in S:
        if len(p) == 3:
            if p[0] == P:
                Q=p[2]
                q=[Q,'→',R]
                if q in S:
                    a=[S.index(p),S.index(q)]
                    tv=True
                    break
    return [tv,['((P→Q),(Q→R)├(P→R))',a]]

def ispremiseexchange(s):
    a=[-1]
    tv=False
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[0][2]) != 3:
        return [False,a]
    P=s[0][0]
    Q=s[0][2][0]
    R=s[0][2][2]
    p=[[P,'→',[Q,'→',R]],'→',[Q,'→',[P,'→',R]]]
    tv=p == s
    if s in S:
        a=[S.index(s)]
    return [tv,['((P→(Q→R))→(Q→(P→R)))',a]]

def isaddantecedent(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    if len(s[2][0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    P=s[2][0][0]
    p=[[Q,'→',R],'→',[[P,'→',Q],'→',[P,'→',R]]]
    tv=p == s
    if s in S:
        a=[S.index(s)]
    return [tv,['((Q→R)→((P→Q)→(P→R)))',a]]

def isaddconsequent(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    if len(s[2][0]) != 3:
        return [False,a]
    P=s[0][0]
    Q=s[0][2]
    R=s[2][0][2]
    p=[[P,'→',Q],'→',[[Q,'→',R],'→',[P,'→',R]]]
    tv=p == s
    if s in S:
        a=[S.index(s)]
    return [tv,['((P→Q)→((Q→R)→(P→R)))',a]]

def isdoublenegation(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[2]
    p=[['¬',['¬',Q]],'→',Q]
    tv=p==s
    if s in S:
        a=[S.index(s)]    
    return [tv,['(¬¬Q→Q)',a]]

def isdoublenegation2(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    p=[Q,'→',['¬',['¬',Q]]]
    tv=p==s
    if s in S:
        a=[S.index(s)]    
    return [tv,['(Q→¬¬Q)',a]]

def isdoublenegation3(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'→',R],'→',[['¬',['¬',Q]],'→',['¬',['¬',R]]]]
    tv=p==s
    if s in S:
        a=[S.index(s)]    
    return [tv,['((Q→R)→(¬¬Q→¬¬R))',a]]

def isdoublenegation4(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][0]
    R=s[2][2]
    p=[[['¬',['¬',Q]],'→',['¬',['¬',R]]],'→',[Q,'→',R]]
    tv=p==s
    if s in S:
        a=[S.index(s)]    
    return [tv,['((¬¬Q→¬¬R)→(Q→R))',a]]

def issinglenegation(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'→',R],'→',[['¬',R],'→',['¬',Q]]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((Q→R)→(¬R→¬Q))',a]]

def issinglenegation2(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][2]
    R=s[0][2]
    p=[[['¬',Q],'→',R],'→',[['¬',R],'→',Q]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((¬Q→R)→(¬R→Q))',a]]

def issinglenegation3(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[2][0]
    p=[[Q,'→',['¬',R]],'→',[R,'→',['¬',Q]]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((Q→¬R)→(R→¬Q))',a]]

def iscontradictorylaw(s):
    a=[-1]
    tv=False
    if len(s) != 2:
        return [False,a]
    if len(s[1]) != 3:
        return [False,a]
    R=s[1][0]
    p=['¬',[R,'∧',['¬',R]]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['(¬(R∧(¬R)))',a]]

def iscontradictoryimplication(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][2]
    R=s[2][0]
    p=[[['¬',Q],'→',Q],'→',[R,'→',Q]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['(((¬Q)→Q)→(R→Q))',a]]

def iscontradictoryimplication2(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[2]
    p=[[['¬',Q],'→',Q],'→',Q]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['(((¬Q)→Q)→Q)',a]]

def iscontradictoryimplication3(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    p=[[Q,'→',['¬',Q]],'→',['¬',Q]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((Q→(¬Q))→(¬Q))',a]]

def isand(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    R=s[2]
    p=[Q,'∧',R]
    q=[['¬',[Q,'→',['¬',R]]]]
    tv=(p==s) and (q in S)
    if (s in S) and (q in S):
        a=[S.index(q),S.index(s)]             
    return [tv,['(Q∧R)≡¬(Q→¬R)',a]]

def isand2(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∧',R],'→',['¬',[Q,'→',['¬',R]]]]
    tv=p==s
    if (s in S):
        a=[S.index(s)]
    return [tv,['(Q∧R)→¬(Q→¬R)',a]]

def isand3(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][0]
    R=s[2][2]
    p=[['¬',[Q,'→',['¬',R]]],'→',[Q,'∧',R]]
    tv=p==s
    if (s in S):
        a=[S.index(s)]
    return [tv,['¬(Q→¬R)→(Q∧R)',a]]

def isand4(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∧',R],'→',Q]
    tv=p==s
    if (s in S):
        a=[S.index(s)]
    return [tv,['((Q∧R)→Q)',a]]

def isand5(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∧',R],'→',R]
    tv=p==s
    if (s in S):
        a=[S.index(s)]
    return [tv,['((Q∧R)→R)',a]]

def isand6(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]

    Q=s[0]
    R=s[2]
    p=[Q,'∧',R]
    tv=(p==s) and (Q in S) and (R in S) and (s in S)
    if tv==True:
        i=S.index(Q)
        j=S.index(R)
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i,j,k]
    return [tv,['Q,R├(Q∧R)',a]]

def isand7(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    P=s[0]
    Q=s[2][0]
    R=s[2][2]
    p=[P,'→',[Q,'∧',R]]
    tv=(p==s) and ([P,'→',Q] in S) and ([P,'→',R] in S) and (s in S)
    if tv==True:
        i=S.index([P,'→',Q])
        j=S.index([P,'→',R])
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i,j,k]
    return [tv,['P→Q,P→R├P→(Q∧R)',a]]

def isand8(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    P=s[0][0]
    Q=s[0][2]
    R=s[2][0]
    S0=s[2][2]
    p=[[P,'∧',Q],'→',[R,'∧',S0]]
    tv=(p==s) and ([P,'→',R] in S) and ([Q,'→',S0] in S) and (s in S)
    if tv==True:
        i=S.index([P,'→',R])
        j=S.index([Q,'→',S0])
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i,j,k]
    return [tv,['P→R,Q→S├(P∧Q)→(R∧S)',a]]

def isor(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    R=s[2]
    p=[Q,'∨',R]
    q=[['¬',Q],'→',R]
    tv=(p==s) and (q in S)
    if s in S and (q in S):
        a=[S.index(q),S.index(s)]             
    return [tv,['(¬Q→R)├(Q∨R)',a]]

def isor1(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∨',R],'→',[['¬',Q],'→',R]]
    tv=(p==s)
    if s in S:
        a=[S.index(s)]             
    return [tv,['(Q∨R)≡(¬Q→R)',a]]

def isor2(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][0]
    R=s[2][2]
    p=[[['¬',Q],'→',R],'→',[Q,'∨',R]]
    tv=(p==s)
    if s in S:
        a=[S.index(s)]             
    return [tv,['(Q∨R)≡(¬Q→R)',a]]

def isor3(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    P=s[0][0]
    Q=s[0][2]
    R=s[2][0]
    S0=s[2][2]
    p=[[P,'∨',Q],'→',[R,'∨',S0]]
    tv=(p==s) and ([P,'→',R] in S) and ([Q,'→',S0] in S) and (s in S)
    if tv==True:
        i=S.index([P,'→',R])
        j=S.index([Q,'→',S0])
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i,j,k]
    return [tv,['P→R,Q→S├(P∨Q)→(R∨S)',a]]

def ispredicatetheorem1(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    if len(s[2]) != 2:
        return [False,a]
    Ax=s[0][0]
    Ay=s[2][0]
    tv=isinstance(Ax,str) and isinstance(Ay,str) and (len(Ax) == 2) and (len(Ay) == 2)
    if tv == False:
        return [False,a]
    x=Ax[1]
    y=Ay[1]
    Qx=s[0][1]
    tv=isinstance(x,str) and isinstance(y,str) and isinstance(Qx,list)
    if tv == False:
        return [False,a]
    Qy=replacechar(Qx,x,y)
    p=[[Ax,Qx],'→',[Ay,Qy]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((∀xQ(x))→(∀yQ(y)))',a]]

def ispredicatetheorem2(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    if len(s[0][1]) != 2:
        return [False,a]
    Ax=s[0][0]
    Ay=s[0][1][0]
    Qxy=s[0][1][1]
    tv=isinstance(Ax,str) and isinstance(Ay,str) and isinstance(Qxy,list)
    tv=tv and Ax[0]=='∀' and Ay[0] == '∀'
    if tv == False:
        return [False,a]
    p=[[Ax,[Ay,Qxy]],'→',[Ay,[Ax,Qxy]]]
    tv=tv and p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['∀x∀yQ(x,y)→∀y∀xQ(x,y)',a]]

def ispredicatetheorem3(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    if len(s[0][1]) != 2:
        return [False,a]
    Ax=s[0][0]
    Ay=s[0][1][0]
    Qxy=s[0][1][1]
    tv=isinstance(Ax,str) and isinstance(Ay,str) and isinstance(Qxy,list)
    tv=tv and Ax[0]=='∀' and Ay[0] == '∀'
    if tv ==False:
        return [False,a]
    x=Ax[1]
    y=Ay[1]
    Qxx=replacechar(Qxy,y,x)
    p=[[Ax,[Ay,Qxy]],'→',[Ax,Qxx]]
    tv=tv and p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['∀x∀yQ(x,y)→∀xQ(x,x)',a]]

def ispredicatetheorem4(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    Ex=s[0][0]
    Q=s[0][1]
    tv=isinstance(Ex,str) and isinstance(Q,list)
    if tv == False:
        return [False,a]
    if Ex[0] != '∃':
        return [False,a]
    x=Ex[1]
    p=[[Ex,Q],'→',['¬',['∀'+x,['¬',Q]]]]
    tv=tv and p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((∃xQ(x))→(¬(∀x(¬Q(x,)))))',a]]

def ispredicatetheorem5(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 2:
        return [False,a]
    if len(s[2][1]) != 2:
        return [False,a]
    Ex=s[2][0]
    Q=s[2][1][1]
    tv=isinstance(Ex,str) and isinstance(Q,list)
    if tv == False:
        return [False,a]
    if Ex[0] != '∃':
        return [False,a]
    x=Ex[1]
    p=[['¬',['∀'+x,Q]],'→',[Ex,['¬',Q]]]
    tv=tv and p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['((¬(∀xQ(x)))→(∃x(¬Q(x))))',a]]

def ispredicatetheorem6(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 2:
        return [False,a]
    Ex=s[2][0]
    Q=s[2][1]
    tv=isinstance(Ex,str) and isinstance(Q,list)
    if tv == False:
        return [False,a]
    if Ex[0] != '∃':
        return [False,a]
    x=Ex[1]
    p=[['¬',['∀'+x,['¬',Q]]],'→',[Ex,Q]]
    tv=tv and p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['(¬(∀x(¬Q(x))))→(∃xQ(x)))',a]]

def ispredicatetheorem7(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 2:
        return [False,a]
    Ex=s[2][0]
    if Ex[0] != '∃':
        return [False,a]
    Q=s[2][1]
    p=[Q,'→',[Ex,Q]]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['(Q(x)→∃xQ(x))',a]]

def ispredicatetheorem8(s):
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    Ex=s[0][0]
    if Ex[0] != '∃':
        return [False,a]
    Q=s[0][1]
    p=[[Ex,Q],'→',Q]
    tv=p==s
    if s in S:
        a=[S.index(s)]
    return [tv,['(∃xQ(x)→Q(x))',a]]

def replace2list(s):
    if LOGIC == 1:
        s=s.replace('P','\'P\'')
        s=s.replace('Q','\'Q\'')
        s=s.replace('R','\'R\'')
        s=s.replace('S','\'S\'')
    s=s.replace('¬','\'¬\',')
    s=s.replace('→',',\'→\',')
    s=s.replace('∨',',\'∨\',')
    s=s.replace('∧',',\'∧\',')
    s=s.replace('∀x','\'∀x\',')
    s=s.replace('∀y','\'∀y\',')
    s=s.replace('∃x','\'∃x\',')
    s=s.replace('∃y','\'∃y\',')
    s=s.replace('P(x)','[\'P\',\'x\']')
    s=s.replace('P(y)','[\'P\',\'y\']')
    s=s.replace('P(x,y)','[\'P\',\'x\',\'y\']')
    s=s.replace('Q(x)','[\'Q\',\'x\']')
    s=s.replace('Q(y)','[\'Q\',\'y\']')
    s=s.replace('Q(c)','[\'Q\',\'c\']')
    s=s.replace('Q(x,y)','[\'Q\',\'x\',\'y\']')
    s=s.replace('Q(x,x)','[\'Q\',\'x\',\'x\']')
    s=s.replace('Q(c,y)','[\'Q\',\'c\',\'y\']')
    s=s.replace('R(x)','[\'R\',\'x\']')
    s=s.replace('R(y)','[\'Q\',\'y\']')
    s=s.replace('R(x,y)','[\'R\',\'x\',\'y\']')
    s=s.replace('(','[')
    s=s.replace(')',']')
    return s

def replace2lists(S):
    Q=""
    k=0
    m=len(S)
    while k <m:
        s=S[k]
        Q=Q+replace2list(s)+","
        k=k+1
    Q=Q.rstrip(",")
    Q=list(eval(Q))
    return Q

def formalverification( ):
    Ev=[]
    k=0
    m=len(S)
    while k<m:
        s=S[k]
        k=k+1
        [tv,a]=isaxiom1schema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaxiom2schema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaxiom3schema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaxiom4schema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaxiom4schema2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaxiom5schema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isMPschema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isUGchema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispremise(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isidentityschema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=istransmissionschema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispremiseexchange(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isdoublenegation(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isdoublenegation2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isdoublenegation3(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isdoublenegation4(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=iscontradictorylaw(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaddantecedent(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isaddconsequent(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=issinglenegation(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=iscontradictoryimplication(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=iscontradictoryimplication2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=iscontradictoryimplication3(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=issinglenegation2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=issinglenegation3(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand3(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand4(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand5(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand6(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand7(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isand8(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isor(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isor1(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isor2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isor3(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=isUGchema(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem1(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem2(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem3(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem4(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem4(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem5(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem6(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem7(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=ispredicatetheorem8(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
        [tv,a]=[False,k-1]
        print("%r"%[tv,a])
    return [tv]

def MathematicalAnalysis( ):
    E=[]
#极限λ
    E=E+[['λ(f(x),x0,a)≡∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))']]
#连续μ
    E=E+[['μ(f(x),x0)≡∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))']]
    E=E+[['μ(f(x),x0,(a,b))≡x0∈(a,b)→∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))']]
#可导τ
    E=E+[['τ(f(x),x0,a)≡∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)-f(x0))/(x-x0)-a|<ε)))']]
    E=E+[['τ(f(x),x0,a)≡∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|Δf(x)/Δx-a|<ε)))']]
#可积ω
    E=E+[['dF(x)=f(x)',
          '├ω(f(x))=F(x)+C']]
#单调函数Λ
    
#极限
#四则运算的极限
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|g(x)-b|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)+g(x))-(a+b)|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)-g(x))-(a-b)|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)*g(x))-(a*b)|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)/g(x))-(a/b)|<ε)))']]
#复合运算
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|g(x)-u0|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(g(x))-a|<ε)))']]
#函数极限性质
#唯一性
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-b|<ε)))',
          '├a==b',
          'ε>0→δ>0∧(|x- x0|<δ→|f(x)-a|<ε))',
          'ε>0→δ>0∧(|x- x0|<δ→|f(x)-b|<ε))',
          'a<b',
          'ε=(b-a)/2',
          'ε>0',
          'δ>0',
          '|x- x0|<δ',
          '|f(x)-a|<ε',
          '|f (x)-b|<ε',
          'f(x)<a+ε=(a+b)/2',
          '(b+a)/2=b-ε<f (x)',
          '(b+a)/2< f (x)∧f (x)< (a+b)/2',
          'a=b']]
#局部有界性
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))',
          '|f(x)|<M',
          '(ε>0→(δ>0∧(|x- x0|<δ→|f(x)-a|<ε))',
           '0<ε<1',
          'δ>0',
          '|x- x0|<δ',
          '|f(x)-a|<ε',
          '|f(x)|<|a|+|f(x)-a|<|a|+ε',
          '|f(x)|<|a|+ε',
          '|f(x)|<|a|+1',
          'M=|a|+1',
          '|f (x)|<M']]
#保序性
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|g(x)-b|<ε)))',
          '∃δ(δ>0∧∀x(|x-x0|<δ→(f(x)≤g(x))',
          '├a≤b',
          '(ε>0→(δ>0∧(|x- x0|<δ→|f(x)-a|<ε))',
          '(ε>0→(δ>0∧(|x- x0|<δ→|g(x)-b|<ε))',
          'a>b',
          'ε=(a-b)/2',
          'δ>0',
          '|x-x0|<δ',
          '|f(x)-a|<ε',
          '|g(x)-b|<ε',
          'a-ε<f(x)',
          '(a+b)/2<f(x)',
          'g(x)<b+ε',
          'g(x)<(a+b)/2',
          '|x-x0|<δ→f(x)≤g(x)',
          'f(x)≤g(x)',
          '(a+b)/2<(a+b)/2',
          'a≤b']]
#夹逼性
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|h(x)-a|<ε)))',
          '∃δ(δ>0∧∀x(|x-x0|<δ→(f(x)≤g(x)∧g(x)≤h(x))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|g(x)-a|<ε)))',
          '(ε>0→(δ>0∧(|x- x0|<δ→|f(x)-a|<ε))',
          '(ε>0→(δ>0∧(|x- x0|<δ→|h(x)-a|<ε))',
          'ε>0',
          'δ>0',
          '|x-x0|<δ',
          '|f (x)-a|<ε',
          '|h(x)-a|<ε',
          'a-ε<f(x)',
          'h(x)<a+ε',
          '|x-x0|<δ→f(x)≤g(x)∧g(x)≤h(x)'
          'f(x)≤g(x)∧g(x)≤h(x)',
          'a-ε<g(x)<a+ε',
          '|g(x)-a|<ε']]
#单侧极限
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(0<x-x0<δ→|f(x)-a|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(0<x0-x<δ→|f(x)-a|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-a|<ε)))']]
#函数连续
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|g(x)-g(x0)|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)+g(x))-(f(x0)+g(x0))|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)-g(x))-(f(x0)-g(x0))|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)*g(x))-(f(x0)*g(x0))|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|(f(x)/g(x))-(f(x0)/g(x0))|<ε)))']]
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|g(x)-g(x0)|<ε)))',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
          '├∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(g(x))-f(g(x0))|<ε)))']]
#区间函数连续
    E=E+[['├x0∈(a,b)∧∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))']]
    E=E+[['├x0∈[a,b]∧∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))']]
#一致连续
    E=E+[['├∀ε(ε>0→∃δ(δ>0∧∀x1∀x0(|x1-x0|<δ→|f(x1)-f(x0)|<ε)))']]
#闭区间函数连续性质
#康托尔（Cantor）定理
    E=E+[['x0∈[a,b]',
          'x1∈[a,b]',
         '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
         '├∀ε(ε>0→∃δ(δ>0∧∀x1∀x0(|x1-x0|<δ→|f(x1)-f(x0)|<ε)))']]
#魏尔斯特拉斯（Weierstrass）第一定理
#有界性
    E=E+[['x0∈[a,b]',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
          '├∃M(M>0∧∀y(y∈[a,b]→|f(y)|<M',
          'x0∈[a,b]',
          '(ε>0→(δ>0∧(|x- x0|<δ→|f(x)-a|<ε))',
          '(ε>0→(δ>0∧(|x1-x0|<δ→|f(x1)-f(x0)|<ε)))',
          'ε>1/2',
          'δ>0',
          '(|x1-x0|<δ→|f(x1)-f(x0)|<ε)',
          'nδ≥(b-a)∧(n-1)δ<(b-a)',
          '|x(k+1)-xk|<δ',
          'xi∈[xk,x(k+1)]∧xj∈[xk,x(k+1)]',
          '|xj-xi|<δ',
          '|f(xi)|<Mi+1/2',
          'M=max{Mi}+1/2',
          '|f(x)|<M']]
#魏尔斯特拉斯（Weierstrass）第二定理
    E=E+[['x0∈[a,b]',
         '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
         '├∀x(x∈[a,b]→(m≤f(x)∧f(x)≤M']]
# 波尔查诺-柯西( Bolzano-Cauchy ）第一定理
    E=E+[['x0∈[a,b]',
          'f(a)*f(b)<0',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
          '├∃ξ(ξ∈[a,b]∧f(ξ)=0']]
# 波尔查诺-柯西( Bolzano-Cauchy ）第二定理
    E=E+[['x0∈[a,b]',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε)))',
          '├∀ζ(f(a)<ζ∧ζ<f(b)→∃ξ(ξ∈[a,b]∧f(ξ)=ζ']]
#导数
    E=E+[['∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|Δf(x)/Δx-a|<ε)))']]
#导数的运算
    E=E+[['df(x)/dx=a',
          'dg(x)/dx=b',
          '├d(f(x)+g(x))/dx=a+b']]
    E=E+[['df(x)/dx=a',
          'dg(x)/dx=b',
          '├d(f(x)-g(x))/dx=a-b']]
    E=E+[['df(x)/dx=a',
          'dg(x)/dx=b',
          '├d(f(x)*g(x))/dx=a*b']]
    E=E+[['df(x)/dx=a',
          'dg(x)/dx=b',
          '├d(f(x)/g(x))/dx=a/b']]
    E=E+[['y=f(u)',
          'u=g(x)',
          'g(x0)=u0',
          '├d(f∘g(x))/dx=df(u)/du*dg(x)/dx']]
    E=E+[['y=f(x)',
          'x=x(t)',
          'y=y(t)',
          '├d(f(x))/dx=(dy(t)/dt)/(dx(t)/dt)']]
#复合函数导数
#反函数导数
#求导方法
#隐函数导数
    E=E+[['y=f(x)',
          'τ(f(x))',
          'F(x,y)=0',
          '├dF(x,y)=0']]
#参数式导数
    E=E+[['y=f(x)',
          'x=x(t)',
          'y=y(t)'
          '├dy/dx=(dy/dt)/(dx/dt)']]
#直角坐标导数
    E=E+[['x=r(θ)*cos(θ)',
          'y=r(θ)*sin(θ)',
          '├dy/dx=(dy/dθ)/(dx/dθ)']]
#极坐标导数
    
#中值定理
    E=E+[['∀x(|x-x0|<δ→f(x)≤f(x0)']]
#费马（Fermat）定理
    E=E+[['∀x(|x-x0|<δ→f(x)≤f(x0)',
          '∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|Δf(x)/Δx-a|<ε)))',
          '├df(x0)/dx=0']]
#罗尔（Rolle）定理
    E=E+[['∀x0(x0∈[a,b]→∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε))))',
          '∀x0(x0∈(a,b)→∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|Δf(x)/Δx-a|<ε)))',
          'f(a)=f(b)',
          '├∃ξ(ξ∈(a,b)→∀ε(ε>0→∃δ(δ>0∧∀x(|x-ξ|<δ→|(f(x)-f(ξ))/Δx-0|<ε))))']]
#拉格朗日（Lagrange）定理
    E=E+[['∀x0(x0∈[a,b]→∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|f(x)-f(x0)|<ε))))',
          '∀x0(x0∈(a,b)→∀ε(ε>0→∃δ(δ>0∧∀x(|x-x0|<δ→|Δf(x)/Δx-a|<ε)))',
          '├∃ξ(ξ∈(a,b)∧∀ε(ε>0→∃δ(δ>0∧∀x(|x-ξ|<δ→|(f(x)-f(ξ))/Δx-((f(b)-f(a))/(b-a))|<ε))))']]
#柯西（Cauchy）定理
    E=E+[['ω(f(x),[a,b])',
          'ω(g(x),[a,b])',
          'τ(f(x),(a,b))',
          'τ(g(x),(a,b))',
          'dg(x)/dx≠0',
          '├∃ξ(ξ∈(a,b)∧((df(ξ)/dx)/(g(ξ)/dx)=((f(b)-f(a))/(b-a))))']]
#不定积分
    E=E+[['∫f(x)+g(x)dx=∫f(x)dx+∫g(x)dx']]
    E=E+[['∫f(x)-g(x)dx=∫f(x)dx-∫g(x)dx']]
    E=E+[['∫kf(x)dx=k∫f(x)dx']]
#换元法
    E=E+[['∫f(u)du=F(u)+C',
          'u=g(x)',
          'τ(g(x))',
          '├∫f(x)(dg(x)/dx)dx=F(g(x))+C']]
    E=E+[['∫f(u)du=F(u)+C',
          'τ(F(u))',
          'u=g(x)',
          'τ(g(x))',
          '├∫f(g(x)x)(dg(x)/dx)dx=∫f(u)du+C']]
    E=E+[['τ(f(x))',
          'τ(g(x))',
          'ω(df(x)/dx*g(x))',
          '├∫f(g(x)x)(dg(x)/dx)dx=f(x)*g(x)-∫(df(x)/dx)*g(x)dx+C']]
#分部积分法
          
#定积分
    E=E+[['∫[a.b]f(x)dx']]
#牛顿-莱布尼兹定理
    E=E+[['μ(f(x),[a,b])',
          '∀x(x∈[a,b]→F(x)=∫f(x)dx)',
          'ω(F(x),[a,b])',
          '∀x(x∈(a,b)→dF(x)/dx=f(x)',
          '├∫[a,b]f(x)dx=F(b)-F(a)']]
    E=E+[['μ(f(x),[a,b])',
          'F(x)=∫[a,x]f(t)dt',
          '├dF(x)/dx=f(x)']]
    E=E+[['μ(f(x),[a,b])',
          'F(x)=∫[a,x]f(t)dt',
          '├μ(F(x),[a,b])']]
    E=E+[['μ(f(x),[a,b])',
          'F(x)=∫[a,x]f(t)dt',
          '├dF(x)/dx=f(x)']]
    E=E+[['μ(f(x),[a,b])',
          'F(φ(x))=∫[a,φ(x)]f(t)dt',
          '├dF(φ(x))/dx=f(x)*dφ(x)/dx']]
    E=E+[['ω(f(x))',
          'ω(g(x))',
          'f(x)≤g(x)',
          '├∫[a,b]f(x)dx≤∫[a,b]g(x)dx']]
    E=E+[['ω(f(x))',
          'ω(|f(x)|)',
          '├|∫[a,b]f(x)dx|≤∫[a,b]|f(x)|dx']]
#定积分线性运算
    E=E+[['a<c<b',
          'ω(f(x),[a,b])',
          'ω(f(x),[a,c])',
          'ω(f(x),[c,b])',
          '├∫[a,b]f(x)dx=∫[a,c]f(x)dx+∫[c,b]f(x)dx']]
#定积分的换元法
    E=E+[['α≤t≤β',
          'a≤φ(t)≤b',
          'φ(α)=a',
          'φ(β)=b',
          'ω(f(x),[a,b])',
          'τ(φ(t),(α,β))',
          '├∫[a,b]f(x)dx= ∫[α,β]f(φ(t))(dφ(t)/dt)dt']]
#分部积分法
    E=E+[['τ(f(x),[a,b])',
          'τ(g(x),[a,b])',
          'ω(df(x)/dx*g(x),[a,b])',
          '├∫[a,b]f(g(x)x)(dg(x)/dx)dx=f(x)*g(x)|[a,b]-∫[a,b](df(x)/dx)*g(x)dx']]
#积分中值定理
    E=E+[['ω(f(x),[a,b])',
          'ω(g(x),[a,b])',
          'ω(f(x)*g(x),[a,b])',
          '∀x(x∈[a,b]→0≤g(x))',
          'm<μ<M',
          '├∫[a,b]f(x)*g(x)dx=μ∫[a,b]g(x)dx']]
    E=E+[['μ(f(x),[a,b])',
          '├∃ξ(ξ∈[a,b]∧∫[a,b]f(x)dx= f(ξ)*(b-a))']]
#积分中值第二定理
    E=E+[['Λ(f(x),[a,b],-1)',
          '0≤f(x)',
          '├∃ξ(ξ∈[a,b]∧∫[a,b]f(x)g(x)dx=f(a)*∫[a,ξ]g(x)dx']]
    E=E+[['Λ(f(x),[a,b],1)',
          '0≤f(x)',
          '├∃ξ(ξ∈[a,b]∧∫[a,b]f(x)g(x)dx=f(b)∫[ξ,b]g(x)dx']]
    E=E+[['Λ(f(x),[a,b],0)',
          '0≤f(x)',
          '├∃ξ(ξ∈[a,b]∧∫[a,b]f(x)g(x)dx=f(a)∫[a,ξ]g(x)dx+f(b)∫[ξ,b]g(x)dx']]
    return E
    
def GodelCode(e):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','ε','δ','α','β','ξ','ζ','θ','Δ','Λ','σ','λ','μ','τ','φ','ω','Σ',
       '>','<','≤','=','≠','∈','≡','├','[',']','+','-','*','/','∘','∫','|',
       'f','g','h','a','b','d','k','x','y','t','u','s','i','n','c','o','r','C','m','M','F','0','1',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149, 151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283,293,307,331,337,
       347,349,353,359,367,383,389,397,401,409,421,443,449,457,461,463,467,487,491,499,
       503,509,521,523,541,547,557,563,569,571,577,587,593,599]
    code=''
    for a in e:
        i=D.index(a)
        code=code+str(P[i])
    return code

def GodelCodes(E):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','ε','δ','α','β','ξ','ζ','θ','Δ','Λ','σ','λ','μ','τ','φ','ω','Σ',
       '>','<','≤','=','≠','∈','≡','├','[',']','+','-','*','/','∘','∫','|',
       'f','g','h','a','b','d','k','x','y','t','u','s','i','n','c','o','r','C','m','M','F','0','1',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149, 151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283,293,307,331,337,
       347,349,353,359,367,383,389,397,401,409,421,443,449,457,461,463,467,487,491,499,
       503,509,521,523,541,547,557,563,569,571,577,587,593,599]
    codes=''
    for e in E:
        codes=codes+GodelCode(e)+'00'
    codes=codes+'22'
    return codes

def GodelDecodes(m):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','ε','δ','α','β','ξ','ζ','θ','Δ','Λ','σ','λ','μ','τ','φ','ω','Σ',
       '>','<','≤','=','≠','∈','≡','├','[',']','+','-','*','/','∘','∫','|',
       'f','g','h','a','b','d','k','x','y','t','u','s','i','n','c','o','r','C','m','M','F','0','1',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149, 151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283,293,307,331,337,
       347,349,353,359,367,383,389,397,401,409,421,443,449,457,461,463,467,487,491,499,
       503,509,521,523,541,547,557,563,569,571,577,587,593,599]
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

def main0( ):
    global Q,R
    E=proofs( )
    Q=[]
    for E0 in E:
        for e in E0:
            e=list(e)
            for k in e:
                Q=Q+[k]
    Q=sorted(Q)
    e0=Q[0]
    n=0
    R=set({})
    for e in Q:
        if e==e0:
            n=n+1
        else:
            R=R|{(n,e0)}
            e0=e
            n=1
    return sorted(R)

def main( ):
    global D,P,E,codes
    D=['(',')','→','¬','∧','∨','↔','∀','∃','P','Q','R','S','x','y','c','├',',',' ']
    P=[3, 5, 7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149, 151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283]
    E=['├∃x(Q(x)∨R(x))→(∃xQ(x)∨∃xR(x))',
          '∀x¬Q(x)→¬Q(x)',
          '∀x¬R(x)→¬R(x)',
          '∀x¬Q(x)∧∀x¬R(x)→¬Q(x)∧¬R(x)',
          '¬Q(x)∧¬R(x)→¬(Q(x)∨R(x))',
          '∀x¬Q(x)∧∀x¬R(x)→¬(Q(x)∨R(x))',
          '¬(¬∀x¬Q(x)∨¬∀x¬R(x))→∀x¬Q(x)∧∀x¬R(x)',
          '¬(¬∀x¬Q(x)∨¬∀x¬R(x))→¬(Q(x)∨R(x))',
          '¬(∃xQ(x)∨∃xR(x))→¬(Q(x)∨R(x))',
          '∀x(¬(∃xQ(x)∨∃xR(x))→¬(Q(x)∨R(x)))',
          '∀x(¬(∃xQ(x)∨∃xR(x))→¬(Q(x)∨R(x)))→¬(∃xQ(x)∨∃xR(x))→∀x¬(Q(x)∨R(x))',
          '¬(∃xQ(x)∨∃xR(x))→∀x¬(Q(x)∨R(x))',
          '(¬(∃xQ(x)∨∃xR(x))→∀x¬(Q(x)∨R(x)))→(¬∀x¬(Q(x)∨R(x))→(∃xQ(x)∨∃xR(x)))',
          '∃x(Q(x)∨R(x))→(∃xQ(x)∨∃xR(x))']
    codes=GodelCodes(E)
    return codes
