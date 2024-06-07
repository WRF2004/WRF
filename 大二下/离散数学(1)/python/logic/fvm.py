
global LOGIC
LOGIC=2
global P
P=[]
global Pfs
Pfs=[]
global S
global Ev
Ev=[]


#定义
#(Q∨R)≡(¬Q→R)
#(Q∧R)≡¬(Q→¬R)
#等值
#¬(Q∧R)=(¬Q∨¬R)
#¬(Q∨R)=(¬Q∧¬R)
#(Q∧R)=¬(¬Q∨¬R)
#(Q∨R)=¬(¬Q∧¬R)
#(Q→R)=¬(Q∧¬R)
#(Q→R)=(¬Q∨R)
#(¬Q→¬R)=¬(¬Q∧R)
#(¬Q→¬R)=(Q∨¬R)
#¬¬Q=Q

#联言命题
#Q∧R
#选言命题
#Q∨R
#假言命题
#Q→R
#负命题
#¬Q
#直言命题
#∀x(Q(x)→R(x))
#∀x(Q(x)→¬R(x))
#∃x(Q(x)∧R(x))
#∃x(Q(x)∧¬R(x))

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
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    P=s[2][0]
    Q=s[0]
    p=[Q,'→',[P,'→',Q]]
    tv=p==s
    Pfs=Pfs+[p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['axiom1',a]]

def isaxiom2schema(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['axiom2',a]]

def isaxiom3schema(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][2]
    R=s[2][0]
    p=[[['¬',Q],'→',['¬',R]]]+['→']+[[R,'→',Q]]
    tv=p == s
    Pfs=Pfs+[p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['axiom3',a]]
#'((∀xQ(x))→Q(x))'
def isaxiom4schema(s):
    global Pfs
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
    Q0=s[0][1]
    Q1=s[2]
    y=Q1[1]
    if Q1[1]=='→':
        t=Q1[0][1]
        tv = (t in ['a', 'b', 'c', 'x', 'y', 'z'])
        t=Q1[2][1]
        tv = tv&(t in ['a', 'b', 'c', 'x', 'y', 'z'])
    elif Q1[1]=='∧':
        t=Q1[0][1]
        tv = (t in ['a', 'b', 'c', 'x', 'y', 'z'])
        t=Q1[2][1]
        tv = tv&(t in ['a', 'b', 'c', 'x', 'y', 'z'])
    else:
        y = Q1[1]
        if len(y)==1:
            t=y[0]
            tv = (t in ['a', 'b', 'c', 'x', 'y', 'z'])
        elif len(y)==2:
            t=y[1]
            tv = (t in ['a', 'b', 'c', 'x', 'y', 'z'])
        elif len(y)==3:
            t=y[1]
            tv = (t in ['a', 'b', 'c', 'x', 'y', 'z'])
            t = y[2]
            tv=tv&(t in ['a', 'b', 'c', 'x', 'y', 'z'])
    p=[[Ax, Q0],'→',Q1]
    tv=tv&(p==[[Ax, Q0],'→',Q1])
    if tv==True:
        k=S.index(s)
        S[k]=p
        a=[k+1]
    return [tv,['axiom4',a]]

def isaxiom5schema(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['axiom5',a]]

def isMPschema(p):
    global Pfs
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
                    a=[S.index(s[0])+1,S.index(s)+1]
                break
    return [tv,['MP',a]]

def isUGchema(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if (s in S) and (Q in S):
        a=[S.index(Q)+1,S.index(s)+1]
    return [tv,['UG',a]]

def ispremise(s):
    global Pfs
    a=[-1]
    tv=s in P
    if s in P:
        a=[P.index(s)+1]
    return [tv,['premise',a]]

def isconclusion(s):
    tv=s == C
    a=[S.index(s)+1]
    return [tv,a]

def isidentityschema(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    p=[Q,'→',Q]
    tv=p == s
    Pfs=Pfs+[p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['(Q→Q)',a]]

def istransmissionschema(s):
    global Pfs
    a=[-1]
    tv=False
    if len(s) != 3:
        return [False,a]
    P=s[0]
    arrow=s[1]
    R=s[2]
    if arrow!='→':
        return [False, a]
    for p in S:
        if len(p) == 3:
            if p[0] == P:
                Q=p[2]
                q=[Q,'→',R]
                if q in S:
                    a=[S.index(p)+1,S.index(q)+1]
                    tv=True
                    break
    return [tv,['((P→Q),(Q→R)├(P→R))',a]]

def ispremiseexchange(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((P→(Q→R))→(Q→(P→R)))',a]]

def isaddantecedent(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((Q→R)→((P→Q)→(P→R)))',a]]

def isaddconsequent(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((P→Q)→((Q→R)→(P→R)))',a]]

def isdoublenegation(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[2]
    p=[['¬',['¬',Q]],'→',Q]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]    
    return [tv,['(¬¬Q→Q)',a]]

def isdoublenegation2(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    p=[Q,'→',['¬',['¬',Q]]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]    
    return [tv,['(Q→¬¬Q)',a]]

def isdoublenegation3(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'→',R],'→',[['¬',['¬',Q]],'→',['¬',['¬',R]]]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]    
    return [tv,['((Q→R)→(¬¬Q→¬¬R))',a]]

def isdoublenegation4(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][0]
    R=s[2][2]
    p=[[['¬',['¬',Q]],'→',['¬',['¬',R]]],'→',[Q,'→',R]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]    
    return [tv,['((¬¬Q→¬¬R)→(Q→R))',a]]

def issinglenegation(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'→',R],'→',[['¬',R],'→',['¬',Q]]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((Q→R)→(¬R→¬Q))',a]]

def issinglenegation2(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((¬Q→R)→(¬R→Q))',a]]

def issinglenegation3(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((Q→¬R)→(R→¬Q))',a]]

def iscontradictorylaw(s):
    global Pfs
    a=[-1]
    tv=False
    if len(s) != 2:
        return [False,a]
    if len(s[1]) != 3:
        return [False,a]
    Q=s[1][0]
    p=['¬',[Q,'∧',['¬',Q]]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['(¬(Q∧(¬Q)))',a]]

def iscontradictoryimplication(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][2]
    R=s[2][0]
    p=[[['¬',Q],'→',Q],'→',[R,'→',Q]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['(((¬Q)→Q)→(R→Q))',a]]

def iscontradictoryimplication2(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[2]
    p=[[['¬',Q],'→',Q],'→',Q]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['(((¬Q)→Q)→Q)',a]]

def iscontradictoryimplication3(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    p=[[Q,'→',['¬',Q]],'→',['¬',Q]]
    tv=p==s
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((Q→(¬Q))→(¬Q))',a]]

def isand(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    R=s[2]
    p=[Q,'∧',R]
    q=[['¬',[Q,'→',['¬',R]]]]
    tv=(p==s) and (q in S)
    Pfs = Pfs + [p]
    if (s in S) and (q in S):
        a=[S.index(q)+1,S.index(s)+1]             
    return [tv,['(Q∧R)≡¬(Q→¬R)',a]]

def isand2(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∧',R],'→',['¬',[Q,'→',['¬',R]]]]
    tv=p==s
    Pfs = Pfs + [p]
    if (s in S):
        a=[S.index(s)+1]
    return [tv,['(Q∧R)≡¬(Q→¬R)',a]]

def isand3(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][0]
    R=s[2][2]
    p=[['¬',[Q,'→',['¬',R]]],'→',[Q,'∧',R]]
    tv=p==s
    Pfs = Pfs + [p]
    if (s in S):
        a=[S.index(s)+1]
    return [tv,['¬(Q→¬R)≡(Q∧R)',a]]

def isand4(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∧',R],'→',Q]
    tv=p==s
    Pfs = Pfs + [p]
    if (s in S):
        a=[S.index(s)+1]
    return [tv,['((Q∧R)→Q)',a]]

def isand5(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∧',R],'→',R]
    tv=p==s
    Pfs = Pfs + [p]
    if (s in S):
        a=[S.index(s)+1]
    return [tv,['((Q∧R)→R)',a]]

def isand6(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]

    Q=s[0]
    R=s[2]
    p=[Q,'∧',R]
    tv=(p==s) and (Q in S) and (R in S) and (s in S)
    Pfs = Pfs + [p]
    if tv==True:
        i=S.index(Q)
        j=S.index(R)
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i+1,j+1,k+1]
    return [tv,['Q,R├(Q∧R)',a]]

def isand7(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if tv==True:
        i=S.index([P,'→',Q])
        j=S.index([P,'→',R])
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i+1,j+1,k+1]
    return [tv,['P→Q,P→R├P→(Q∧R)',a]]

def isand8(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if tv==True:
        i=S.index([P,'→',R])
        j=S.index([Q,'→',S0])
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i+1,j+1,k+1]
    return [tv,['P→R,Q→S├(P∧Q)→(R∧S)',a]]

def isor(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    Q=s[0]
    R=s[2]
    p=[Q,'∨',R]
    q=[['¬',Q],'→',R]
    tv=(p==s) and (q in S)
    Pfs = Pfs + [p]
    if s in S and (q in S):
        a=[S.index(q)+1,S.index(s)+1]             
    return [tv,['(¬Q→R)≡(Q∨R)',a]]

def isor1(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 3:
        return [False,a]
    Q=s[0][0]
    R=s[0][2]
    p=[[Q,'∨',R],'→',[['¬',Q],'→',R]]
    tv=(p==s)
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]             
    return [tv,['(Q∨R)≡(¬Q→R)',a]]

def isor2(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 3:
        return [False,a]
    Q=s[2][0]
    R=s[2][2]
    p=[[['¬',Q],'→',R],'→',[Q,'∨',R]]
    tv=(p==s)
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]             
    return [tv,['(Q∨R)≡(¬Q→R)',a]]

def isor3(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if tv==True:
        i=S.index([P,'→',R])
        j=S.index([Q,'→',S0])
        k=S.index(s)
        tv=(i < k) and (j < k)
        if tv == True:
            a=[i+1,j+1,k+1]
    return [tv,['P→R,Q→S├(P∨Q)→(R∨S)',a]]

def ispredicatetheorem1(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((∀xQ(x))→(∀yQ(y)))',a]]

def ispredicatetheorem2(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['∀x∀yQ(x,y)→∀y∀xQ(x,y)',a]]

def ispredicatetheorem3(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['∀x∀yQ(x,y)→∀xQ(x,x)',a]]

def ispredicatetheorem4(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((∃xQ(x))→(¬(∀x(¬Q(x,)))))',a]]

def ispredicatetheorem5(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['((¬(∀xQ(x)))→(∃x(¬Q(x))))',a]]

def ispredicatetheorem6(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
    return [tv,['(¬(∀x(¬Q(x))))≡(∃xQ(x)))',a]]

def ispredicatetheorem7(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[2]) != 2:
        return [False,a]
    Ex=s[2][0]
    Qc=s[0]
    if Ex[0] != '∃':
        return [False,a]
    Q=s[2][1]
    x=Qc[1]
    tv=x in ['a','b','c','x','y','z']
    p=[Qc,'→',[Ex,Q]]
    tv=tv&(p==s)
    Pfs = Pfs + [p]
    if tv==True:
        a=[S.index(s)+1]
    return [tv,['(Q(c)→∃xQ(x))',a]]

#'((∃xQ(x))→(Q(c)))'
def ispredicatetheorem8(s):
    global Pfs
    a=[-1]
    if len(s) != 3:
        return [False,a]
    if len(s[0]) != 2:
        return [False,a]
    Ex=s[0][0]
    if Ex[0] != '∃':
        return [False,a]
    Q0=s[0][1]
    Q1=s[2]
    p=[[Ex,Q0],'→',Q1]
    tv=(p==[[Ex,Q0],'→',Q1])
    Pfs = Pfs + [p]
    if s in S:
        k=S.index(s)
        S[k]=p
        a=[k+1]
    return [tv,['(∃xQ(x)→Q(c))',a]]

def ispredicatetheorem80(s):
    global Pfs
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
    Pfs = Pfs + [p]
    if s in S:
        a=[S.index(s)+1]
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
    s = s.replace('[', ',[')
    s = s.replace('/', ',')
    s=s.replace('P(x)','[\'P\',\'x\']')
    s=s.replace('P(y)','[\'P\',\'y\']')
    s=s.replace('P(x,y)','[\'P\',\'x\',\'y\']')
    s=s.replace('Q(x)','[\'Q\',\'x\']')
    s=s.replace('Q(y)','[\'Q\',\'y\']')
    s = s.replace('P(a)', '[\'P\',\'a\']')
    s = s.replace('Q(b)', '[\'Q\',\'b\']')
    s = s.replace('R(c)', '[\'R\',\'c\']')
    s=s.replace('P(c)','[\'P\',\'c\']')
    s=s.replace('Q(c)','[\'Q\',\'c\']')
    s=s.replace('R(c)','[\'R\',\'c\']')
    s=s.replace('Q(x,y)','[\'Q\',\'x\',\'y\']')
    s=s.replace('Q(x,x)','[\'Q\',\'x\',\'x\']')
    s = s.replace('Q(x,b)', '[\'Q\',\'x\',\'b\']')
    s = s.replace('Q(a,y)', '[\'Q\',\'a\',\'y\']')
    s = s.replace('Q(b,y)', '[\'Q\',\'b\',\'y\']')
    s=s.replace('Q(c,y)','[\'Q\',\'c\',\'y\']')
    s = s.replace('Q(a,b)', '[\'Q\',\'a\',\'b\']')
    s=s.replace('R(x)','[\'R\',\'x\']')
    s=s.replace('R(y)','[\'Q\',\'y\']')
    s=s.replace('R(x,y)','[\'R\',\'x\',\'y\']')
    s = s.replace('[x,x]', '[\'x\',\'x\']')
    s = s.replace('[x,y]', '[\'x\',\'y\']')
    s = s.replace('[x,c]', '[\'x\',\'c\']')
    s = s.replace('[y,c]', '[\'y\',\'c\']')
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

def subsvar(x,t,s):
    if isinstance(s,str):
        if s==x:
            s=t
        return s
    Q=[]
    for e in s:
        k=s.index(e)
        Q=Q+[subsvar(x,t,e)]
    return Q

#formalverification
def fvm(E):
    global P
    global S
    if P != list({}):
        if len(P)==1:
            P=[replace2lists(P)]
        else:
            P = replace2lists(P)
    S=replace2lists(E)
    Ev=[]
    k=0
    m=len(S)
    while k<m:
        s=S[k]
        k=k+1
        [tv,a]=ispremise(s)
        if tv == True:
            print("%r"%[tv,a])
            Ev=Ev+[a]
            continue
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

def proofs( ):
    global E
    E=[]
#肯定前件（Modus Ponens）
#(Q→R),Q├R
    E=E+['(Q→R)',
         'Q',
         'R']
#否定后件（Modus Tollens）
#(Q→R), ¬R├¬Q
    E=E+[['(Q→R), ¬R├¬Q',
          '(Q→R)',
          '((Q→R)→((¬R)→(¬Q)))',
          '((¬R)→(¬Q))',
          '(¬R)',
          '(¬Q)']]
#析取三段论（Disjunctive Syllogism）
#(Q∨R),¬Q ├R
    E=E+[['(Q∨R),¬Q├R',
          '((¬Q)→R)',
          '(¬Q)',
          'R']]
#假言三段论（Hypothetical Syllogism）
#(P→Q), (Q→R)├ (P→R)
#简化式（Simplification）
#Q∧R├Q
#组合式（Conjunction）
#Q,R ├Q∧R
#附加式（Addition）
#Q ├ Q∨R
#二难构成式（Constructive Dilemma）
#(P∨Q), (P→R), (Q→S) ├R∨S
#双重否定律（Double Negation）
#Q ├ ¬¬Q
    E=E+[['Q ├ ¬¬Q',
          '(Q→(¬(¬Q)))',
          'Q',
          '(¬(¬Q)))']]
#德摩根律（ DeMorgan's Theorem ）
#¬(Q∨R)├(¬Q∧¬R)
#¬(Q∧R)├(¬Q∨¬R)
#交换律（Commutation）
#(Q∧R)├ (R∧Q)
#(Q∨R)├ (R∨Q)
#结合律（association）
#(P∧(Q∧R))├ ((P∧Q)∧R)
#(P∨(Q∨R))├ ((P∨Q)∨R)
#分配律（distribution）
#(P∧(Q∨R))├ ((P∧Q)∨(P∧R))
#(P∨(Q∧R))├ ((P∨Q)∧(P∨R))
#移位律（contraposition）
#(Q→R)├(¬R→¬Q)
#移出律（exportation）
#(P∧Q)→R├ (P→(Q→R))
#重言律（ tautology ）
#Q ├ (Q∧Q)
#Q├ (Q∨Q)

    E=E+[['(P→Q)','(Q→R)','├(P→R)',
          '((Q→R)→(P→(Q→R)))',
          '(Q→R)',
          '(P→(Q→R))',
         '((P→(Q→R))→((P→Q)→(P→R)))',
          '((P→Q)→(P→R))',
          '(P→Q)',
          '(P→R)']]
    E=E+[['P', '(Q→(P→R))','├(Q→R)',
          '(Q→(P→R))',
          '((Q→(P→R))→((Q→P)→(Q→R)))',
          '((Q→P)→(Q→R))',
          '(P→(Q→P))', 
          'P',
          '(Q→P)',
          '(Q→R)']]
    E=E+[['├((¬Q)→(Q→R))',
          '((¬Q)→((¬R)→(¬Q)))',
          '(((¬R)→(¬Q))→(Q→R))',
          '((¬Q)→(Q→R))']]
    E=E+[['├((P→(Q→R))→(Q→(P→R)))',
          '((P→(Q →R))→((P→Q)→(P→R)))',
          '(((P→Q)→(P→R))→(Q→((P→Q)→(P→R))))',
          '((Q→((P→Q)→(P→R)))→((Q→(P→Q))→(Q→(P→R))))',
          '((P→(Q →R))→(Q→((P→Q)→(P→R))))',
          '((P→(Q→R))→((Q→(P→Q))→(Q→(P→R))))',
          '(Q→(P→Q))',
          '((P→(Q→R))→(Q→(P→R)))']]
    E=E+[['├((P→(Q→R))→(Q→(P→R)))',
          '((P→(Q→R))→((P→Q)→(P→R)))',
          '(((P→Q)→(P→R))→(Q→((P→Q)→(P→R))))',
          '((P→(Q→R))→(Q→((P→Q)→(P→R))))',
          '((Q→((P→Q)→(P→R)))→((Q→(P→Q))→(Q→(P→R))))',
          '((P→(Q→R))→((Q→(P→Q))→(Q→(P→R))))',
          '(((P→(Q→R))→((Q→(P→Q))→(Q→(P→R))))→(((P→(Q→R))→(Q→(P→Q)))→((P→(Q→R))→(Q→(P→R)))))',
          '(((P→(Q→R))→(Q→(P→Q)))→((P→(Q→R))→(Q→(P→R))))',
          '(Q→(P→Q))',
          '((Q→(P→Q))→((P→(Q→R))→(Q→(P→Q))))',
          '((P→(Q→R))→(Q→(P→Q)))',
          '((P→(Q→R))→(Q→(P→R)))']]
    E=E+[['├(Q→Q)',
          '(Q→((Q→(Q→Q))→Q))',
          '((Q→((Q→(Q→Q))→Q))→((Q→(Q→Q))→(Q→Q)))',
          '((Q→(Q→Q))→(Q→Q))',
          '(Q→(Q→Q))',
          '(Q→Q)']]
    E=E+[['├((Q→R)→((P→Q)→(P→R)))',
          '((Q→R)→(P→(Q→R)))',
          '((P→(Q→R))→((P→Q)→(P→R)))',
          '((Q→R)→((P→Q)→(P→R)))']]
    E=E+[['├((P→Q)→((Q→R)→(P→R)))',
          '((Q→R)→(P→(Q→R)))',
          '((P→(Q→R))→((P→Q)→(P→R)))',
          '((Q→R)→((P→Q)→(P→R)))',
          '(((Q→R)→((P→Q)→(P→R)))→((P→Q)→((Q→R)→(P→R))))',
          '((P→Q)→((Q→R)→(P→R)))']]
    E=E+[['├((¬(¬Q))→Q)',
          '((¬(¬Q))→((¬(¬(¬(¬Q))))→(¬(¬Q))))',
          '(((¬(¬(¬(¬Q))))→(¬(¬Q)))→((¬Q)→(¬(¬(¬Q)))))',
          '(((¬Q)→(¬(¬(¬Q))))→((¬(¬Q))→Q))',
          '((¬(¬Q))→((¬(¬Q))→Q))',
          '(((¬(¬Q))→((¬(¬Q))→Q))→(((¬(¬Q))→(¬(¬Q)))→((¬(¬Q))→Q)))',
          '(((¬(¬Q))→(¬(¬Q)))→((¬(¬Q))→Q))',
          '((¬(¬Q))→(¬(¬Q)))',
          '((¬(¬Q))→Q)']]
    E=E+[['├(Q→(¬(¬Q)))',
          '(((¬(¬(¬Q)))→(¬Q))→(Q→(¬(¬Q))))',
          '((¬(¬(¬Q)))→(¬Q))',
          '(Q→(¬(¬Q)))']]
    E=E+[['├(((¬(¬Q))→(¬(¬R)))→(Q→R))',
          '(((¬(¬Q))→(¬(¬R)))→((¬R)→(¬Q)))',
          '(((¬R)→(¬Q))→(Q→R))',
          '(((¬(¬Q))→(¬(¬R)))→(Q→R))']]
    E=E+[['├((Q→R)→((¬(¬Q))→(¬(¬R))))',
          '(R→(¬(¬R)))',
          '((R→(¬(¬R)))→((¬(¬Q))→(R→(¬(¬R)))))',
          '((¬(¬Q))→(R→(¬(¬R))))',
          '(((¬(¬Q))→(R→(¬(¬R))))→(((¬(¬Q))→R)→((¬(¬Q))→(¬(¬R)))))',
          '(((¬(¬Q))→R)→((¬(¬Q))→(¬(¬R))))',
          '((¬(¬Q))→Q)',
          '(((¬(¬Q))→Q)→((Q→R)→((¬(¬Q))→R)))',
          '((Q→R)→((¬(¬Q))→R))',
          '((Q→R)→((¬(¬Q))→(¬(¬R))))']]
    E=E+[['├((Q→R)→((¬R)→(¬Q)))',
          '((Q→R)→((¬(¬Q))→(¬(¬R))))',
          '(((¬(¬Q))→(¬(¬R)))→((¬R)→(¬Q)))',
          '((Q→R)→((¬R)→(¬Q)))']]
    E=E+[['├(((¬Q)→R)→((¬R)→Q))',
          '((¬(¬Q))→Q)',
          '(((¬(¬Q))→Q)→(((¬R)→(¬(¬Q)))→((¬R)→Q)))',
          '(((¬R)→(¬(¬Q)))→((¬R)→Q))',
          '(((¬Q)→R)→((¬R)→(¬(¬Q))))',
          '(((¬Q)→R)→((¬R)→Q))']]
    E=E+[['├((Q→(¬R))→(R→(¬Q)))',
          '(((¬(¬Q))→Q)→((Q→(¬R))→((¬(¬Q))→(¬R))))',
          '((¬(¬Q))→Q)',
          '((Q→(¬R))→((¬(¬Q))→(¬R)))',
          '(((¬(¬Q))→(¬R))→(R→(¬Q)))',
          '((Q→(¬R))→(R→(¬Q)))']]
    E=E+[['├((¬Q)→(Q→R))',
          '((¬Q)→((¬R)→(¬Q)))',
          '(((¬R)→(¬Q))→(Q→R))',
          '((¬Q)→(Q→R))']]
    E=E+[['├((Q→R)→((¬R)→(¬Q)))',
          '((Q→R)→((¬(¬Q))→(¬(¬R))))',
          '(((¬(¬Q))→(¬(¬R)))→((¬R)→(¬Q)))',
          '((Q→R)→((¬R)→(¬Q)))']]
    E=E+[['├(((¬Q)→R)→((¬R)→Q))',
          '(((¬Q)→R)→((¬R)→(¬(¬Q))))',
          '((¬(¬Q))→Q)',
          '(((¬(¬Q))→Q)→(((¬R)→(¬(¬Q)))→((¬R)→Q)))',
          '(((¬R)→(¬(¬Q)))→((¬R)→Q))',
          '(((¬Q)→R)→((¬R)→Q))']]
    E=E+[['├(((¬Q)→Q)→(R→Q))',
          '((¬Q)→((¬(¬R))→(¬Q)))',
          '(((¬(¬R))→(¬Q))→(Q→(¬R)))',
          '((¬Q)→(Q→(¬R)))',
          '(((¬Q)→(Q→(¬R)))→(((¬Q)→Q)→((¬Q)→(¬R))))',
          '(((¬Q)→Q)→((¬Q)→(¬R)))',
          '(((¬Q)→(¬R))→(R→Q))',
          '(((¬Q)→Q)→(R→Q))']]
    E=E+[['├(((¬Q)→Q)→Q)',
          '(((¬Q)→Q)→(((¬Q)→Q)→Q))',
          '((((¬Q)→Q)→(((¬Q)→Q)→Q))→((((¬Q)→Q)→((¬Q)→Q))→(((¬Q)→Q)→Q)))',
         '((((¬Q)→Q)→((¬Q)→Q))→(((¬Q)→Q)→Q))',
         '(((¬Q)→Q)→((¬Q)→Q))',
         '(((¬Q)→Q)→Q)']]
    E=E+[['├((Q∨Q)→Q)',
          '((Q∨Q)→((¬Q)→Q))',
          '(((¬Q)→Q)→Q)',
          '((Q∨Q)→Q)']]
    E=E+[['├(¬(Q∧(¬Q)))',
          '(Q→(¬(¬Q)))',
          '((Q→(¬(¬Q)))→(¬(¬(Q→(¬(¬Q))))))',
          '(¬(¬(Q→(¬(¬Q)))))',
          '(¬(Q∧(¬Q)))']]
    E=E+[['├(Q∨(¬Q))',
          '((¬Q)→(¬Q))',
          '(Q∨(¬Q))']]    
    E=E+[['├((Q→R)∨(R→Q))',
          '((¬Q)→((¬R)→(¬Q)))',
          '(((¬R)→(¬Q))→(Q→R))',
          '((¬Q)→(Q→R))',
          '(((¬Q)→(Q→R))→((¬(Q→R))→Q))',
          '((¬(Q→R))→Q)',
          '(Q→(R→Q))',
          '((¬(Q→R))→(R→Q))',
          '((Q→R)∨(R→Q))']]
    E=E+[['├((Q→R)∨(R→Q))',
          '((¬Q)→((¬R)→(¬Q)))',
          '(((¬R)→(¬Q))→(Q→R))',
          '((¬Q)→(Q→R))',
          '(((¬Q)→(Q→R))→(R→((¬Q)→(Q→R))))',
          '(R→((¬Q)→(Q→R)))',
          '(((¬Q)→(Q→R))→((¬(Q→R))→Q))',
          '(R→((¬(Q→R))→Q))',
          '((R→((¬(Q→R))→Q))→((¬(Q→R))→(R→Q)))',
          '((¬(Q→R))→(R→Q))',
          '((Q→R)∨(R→Q))']]
    E=E+[['├((Q→R)∨(Q→(¬R)))',
          '(R→(Q→R))',
          '((R→(Q→R))→(Q→(R→(Q→R))))',
          '(Q→(R→(Q→R)))',
          '((R→(Q→R))→((¬(Q→R))→(¬R)))',
          '(Q→((¬(Q→R))→(¬R)))',
         '((Q→((¬(Q→R))→(¬R)))→((¬(Q→R))→(Q→(¬R))))',
          '((¬(Q→R))→(Q→(¬R)))',
          '((Q→R)∨(Q→(¬R)))']]
    E=E+[['├((Q∧(Q→R))→R)',
          '((Q→R)→(Q→R))',
          '(((Q→R)→(Q→R))→(Q→((Q→R)→R)))',
          '(Q→((Q→R)→R))',
          '(((Q→R)→R)→((¬R)→(¬(Q→R))))',
          '(Q→((¬R)→(¬(Q→R))))',
          '((Q→((¬R)→(¬(Q→R))))→((¬R)→(Q→(¬(Q→R)))))',
          '((¬R)→(Q→(¬(Q→R))))',
          '(((¬R)→(Q→(¬(Q→R))))→((¬(Q→(¬(Q→R))))→R))',
          '((¬(Q→(¬(Q→R))))→R)',
          '((Q∧(Q→R))→(¬(Q→(¬(Q→R)))))',
          '(((Q∧(Q→R))→(¬(Q→(¬(Q→R)))))→(((¬(Q→(¬(Q→R))))→R)→((Q∧(Q→R))→R)))',
          '(((¬(Q→(¬(Q→R))))→R)→((Q∧(Q→R))→R))',
          '((Q∧(Q→R))→R)']]
    E=E+[['├(((¬Q)→R)→(((¬Q)→(¬R))→Q))',
          '(((¬Q)→R)→((¬Q)→((¬Q)→R)))',
          '(((¬Q)→R)→((¬R)→Q))',
          '((((¬Q)→R)→((¬R)→Q))→(((¬Q)→((¬Q)→R))→((¬Q)→((¬R)→Q))))',
          '(((¬Q)→((¬Q)→R))→((¬Q)→((¬R)→Q)))',
          '(((¬Q)→R)→((¬Q)→((¬R)→Q)))',
          '(((¬Q)→((¬R)→Q))→(((¬Q)→(¬R))→((¬Q)→Q)))',
          '(((¬Q)→R)→(((¬Q)→(¬R))→((¬Q)→Q)))',
          '(((¬Q)→Q)→Q)',
          '((((¬Q)→Q)→Q)→((((¬Q)→(¬R))→((¬Q)→Q))→(((¬Q)→(¬R))→Q)))',
          '((((¬Q)→(¬R))→((¬Q)→Q))→(((¬Q)→(¬R))→Q))',
          '(((¬Q)→R)→(((¬Q)→(¬R))→Q))']]
    E=E+[['├((Q→R)→((Q→(¬R))→(¬Q)))',
          '((Q→R)→(Q→(Q→R)))',
          '((Q→R)→((¬R)→(¬Q)))',
          '(((Q→R)→((¬R)→(¬Q)))→((Q→(Q→R))→(Q→((¬R)→(¬Q)))))',
          '((Q→(Q→R))→(Q→((¬R)→(¬Q))))',
          '((Q→R)→(Q→((¬R)→(¬Q))))',
          '((Q→((¬R)→(¬Q)))→((Q→(¬R))→(Q→(¬Q))))',
          '((Q→R)→((Q→(¬R))→(Q→(¬Q))))',
          '((Q→(¬Q))→(¬Q))',
          '(((Q→(¬Q))→(¬Q))→(((Q→(¬R))→(Q→(¬Q)))→((Q→(¬R))→(¬Q))))',
          '(((Q→(¬R))→(Q→(¬Q)))→((Q→(¬R))→(¬Q)))',
          '((Q→R)→((Q→(¬R))→(¬Q)))']]
    E=E+[['├(((¬Q)→(R∧(¬R)))→Q)',
          '(((¬Q)→(R∧(¬R)))→((¬(R∧(¬R)))→Q))',
          '((((¬Q)→(R∧(¬R)))→((¬(R∧(¬R)))→Q))→((((¬Q)→(R∧(¬R)))→(¬(R∧(¬R))))→(((¬Q)→(R∧(¬R)))→Q)))',
         '((((¬Q)→(R∧(¬R)))→(¬(R∧(¬R))))→(((¬Q)→(R∧(¬R)))→Q))',
          '(¬(R∧(¬R)))',
          '((¬(R∧(¬R)))→(((¬Q)→(R∧(¬R)))→(¬(R∧(¬R)))))',
          '(((¬Q)→(R∧(¬R)))→(¬(R∧(¬R))))',
          '(((¬Q)→(R∧(¬R)))→Q)']]
    E=E+[['├(Q→(R∨Q))',
          '(Q→((¬R)→Q))',
          '(((¬R)→Q)→(R∨Q))',
          '(Q→(R∨Q))']]
    E=E+[['├((Q∧R)→(R∧Q))',
          '((R→(¬Q))→(Q→(¬R)))',
          '(((R→(¬Q))→(Q→(¬R)))→((¬(Q→(¬R)))→(¬(R→(¬Q)))))',
          '((¬(Q→(¬R)))→(¬(R→(¬Q))))',
          '((Q∧R)→(¬(Q→(¬R))))',
          '((Q∧R)→(¬(R→(¬Q))))',
          '((¬(R→(¬Q)))→(R∧Q))',
          '((Q∧R)→(R∧Q))']]
    E=E+[['├((Q∧R)→Q)',
          '((¬Q)→(R→(¬Q)))',
          '((R→(¬Q))→(Q→(¬R)))',
          '((¬Q)→(Q→(¬R)))',
          '(((¬Q)→(Q→(¬R)))→((¬(Q→(¬R)))→Q))',
          '((¬(Q→(¬R)))→Q)',
          '((Q∧R)→(¬(Q→(¬R))))',
          '((Q∧R)→Q)']]
    E=E+[['├(Q→(R→(Q∧R)))',
          '((Q→(¬R))→(Q→(¬R)))',
          '(((Q→(¬R))→(Q→(¬R)))→(Q→((Q→(¬R))→(¬R))))',
          '(Q→((Q→(¬R))→(¬R)))',
         '(((Q→(¬R))→(¬R))→(R→(¬(Q→(¬R)))))',
         '(Q→(R→(¬(Q→(¬R)))))',
          '((¬(Q→(¬R)))→(Q∧R))',
          '(((¬(Q→(¬R)))→(Q∧R))→((R→(¬(Q→(¬R))))→(R→(Q∧R))))',
          '((R→(¬(Q→(¬R))))→(R→(Q∧R)))',
         '(Q→(R→(Q∧R)))']]
    E=E+[['├(((P∧Q)→R)→(P→(Q→R)))',
          '(((P∧Q)→R)→((¬R)→(¬(P∧Q))))',          
          '((¬(P→(¬Q)))→(P∧Q))',
          '(((¬(P→(¬Q)))→(P∧Q))→((¬(P∧Q))→(P→(¬Q))))',
          '((¬(P∧Q))→(P→(¬Q)))',
          '(((¬(P∧Q))→(P→(¬Q)))→(((¬R)→(¬(P∧Q)))→((¬R)→(P→(¬Q)))))',
          '(((¬R)→(¬(P∧Q)))→((¬R)→(P→(¬Q))))',
          '(((P∧Q)→R)→((¬R)→(P→(¬Q))))',
          '(((¬R)→(P→(¬Q)))→(P→((¬R)→(¬Q))))',
          '(((P∧Q)→R)→(P→((¬R)→(¬Q))))',
          '(((¬R)→(¬Q))→(Q→R))',
          '((((¬R)→(¬Q))→(Q→R))→(P→(((¬R)→(¬Q))→(Q→R))))',
          '(P→(((¬R)→(¬Q))→(Q→R)))',
          '((P→(((¬R)→(¬Q))→(Q→R)))→((P→((¬R)→(¬Q)))→(P→(Q→R))))',
          '((P→((¬R)→(¬Q)))→(P→(Q→R)))',
         '(((P∧Q)→R)→(P→(Q→R)))']]

    E=E+[['├(Q→((¬R)→(¬(Q→R))))',
          '((Q→R)→(Q→R))',
          '(((Q→R)→(Q→R))→(Q→((Q→R)→R)))',
          '(Q→((Q→R)→R))',
          '(((Q→R)→R)→((¬R)→(¬(Q→R))))',
          '(Q→((¬R)→(¬(Q→R))))']]

    E=E+[['├(((P→Q)→(P→R))→(P→(Q→R)))']]    
    E=E+[['├(((P→Q)∧(P→R))→(P→(Q∧R)))']]
    E=E+[['├((P→R)→((Q→R)→((P∨Q)→R)))']]
    E=E+[['├((Q→R)→((P∧Q)→(P∧R)))']]
    E=E+[['├((Q→R)→((P∨Q)→(P∨R)))']]
    E=E+[['├(((P→R)∧(Q→S))→((P∨Q)→(R∨S)))']]
    E=E+[['Q,R├(Q∧R)',
          '((Q→(¬R))→(Q→(¬R)))',
          '(((Q→(¬R))→(Q→(¬R)))→(Q→((Q→(¬R))→(¬R))))',
          '(Q→((Q→(¬R))→(¬R)))',
          'Q',
          '((Q→(¬R))→(¬R))',
          '(((Q→(¬R))→(¬R))→(R→(¬(Q→(¬R)))))',
          '(R→(¬(Q→(¬R))))',
          'R',
          '(¬(Q→(¬R)))',
          '((¬(Q→(¬R)))→(Q∧R))',
          '(Q∧R)']]
    E=E+[['├(((P→R)∧(Q→S))→((P∧Q)→(R∧S)))',
          '(P→R)','(Q→S)','P','Q','├R∧S',
           '(P→R)',
           '(Q→S)',
           'P',
           'Q',
           'R',
           'S',
           '(R∧S)']]
    
    E=E+[['├((∀xQ(x))→(∀yQ(y)))',
          '((∀xQ(x))→Q(y))',
          '(∀y((∀xQ(x))→Q(y)))',
          '((∀y((∀xQ(x))→Q(y)))→((∀xQ(x))→(∀yQ(y))))',
          '((∀xQ(x))→(∀yQ(y)))']]  
    E=E+[['├((∃xQ(x))→(∃yQ(y)))',
          '((∀y(¬Q(y)))→(∀x(¬Q(x))))',
          '(((∀y(¬Q(y)))→(∀x(¬Q(x))))→((¬(∀x(¬Q(x))))→(¬(∀y(¬Q(y))))))',
          '((¬(∀x(¬Q(x))))→(¬(∀y(¬Q(y)))))',
          '((∃xQ(x))→(∃yQ(y)))']]
    E=E+[['├(Q(c)→(∃xQ(x)))',
          '((∀x(¬Q(x)))→(¬Q(c)))',
          '(((∀x(¬Q(x)))→(¬Q(c)))→(Q(c)→(¬(∀x(¬Q(x))))))',
          '(Q(c)→(¬(∀x(¬Q(x)))))',
          '((¬(∀x(¬Q(x))))→(∃xQ(x)))',
          '(Q(c)→(∃xQ(x)))']]
    E=E+[['├((∀xQ(x))→(∃xQ(x)))',
          '((∀xQ(x))→Q(c))',
          '(Q(c)→(∃xQ(x)))',
          '((∀xQ(x))→(∃xQ(x)))']]
    E=E+[['├((∀x(∀yQ(x,y)))→(∀y(∀xQ(x,y))))',
          '((∀x(∀yQ(x,y)))→(∀yQ(x,y)))',
          '((∀yQ(x,y))→Q(x,y))',
          '((∀x(∀yQ(x,y)))→Q(x,y))',
          '(∀x((∀x(∀yQ(x,y)))→Q(x,y)))',
          '((∀x((∀x(∀yQ(x,y)))→Q(x,y)))→((∀x(∀yQ(x,y)))→(∀xQ(x,y))))',
          '((∀x(∀yQ(x,y)))→(∀xQ(x,y)))',
          '(∀y((∀x(∀yQ(x,y)))→(∀xQ(x,y))))',
          '((∀y((∀x(∀yQ(x,y)))→(∀xQ(x,y))))→((∀x(∀yQ(x,y)))→(∀y(∀xQ(x,y)))))',
          '((∀x(∀yQ(x,y)))→(∀y(∀xQ(x,y))))']]
##
    E=E+[['├((∃x(∃yQ(x,y)))→(∃y(∃xQ(x,y))))',
          '((∀y(∀x(¬Q(x,y))))→(∀x(∀y(¬Q(x,y)))))',
          '(((∀y(∀x(¬Q(x,y))))→(∀x(∀y(¬Q(x,y)))))→((¬(∀x(∀y(¬Q(x,y)))))→(¬(∀y(∀x(¬Q(x,y)))))))',
          '((¬(∀x(∀y(¬Q(x,y)))))→(¬(∀y(∀x(¬Q(x,y))))))',
          '((∃x(¬(∀y(¬Q(x,y)))))→(∃y(¬(∀x(¬Q(x,y))))))',
          '((∃x(∃yQ(x,y)))→(∃y(∃xQ(x,y))))']]
    E=E+[['├((∀x(∀yQ(x,y)))→(∀xQ(x,x)))',
          '((∀x(∀yQ(x,y)))→(∀yQ(x,y)))',
          '((∀yQ(x,y))→Q(x,x))',
          '((∀x(∀yQ(x,y)))→Q(x,x))',
          '(∀x((∀x(∀yQ(x,y)))→Q(x,x)))',
          '((∀x((∀x(∀yQ(x,y)))→Q(x,x)))→((∀x(∀yQ(x,y)))→(∀xQ(x,x))))',
          '((∀x(∀yQ(x,y)))→(∀xQ(x,x)))']]
##
    E=E+[['├((∃xQ(x,x))→(∃x(∃yQ(x,y))))',
          '((∀x(∀y(¬Q(x,y))))→(∀x(¬Q(x,x))))',
          '(((∀x(∀y(¬Q(x,y))))→(∀x(¬Q(x,x))))→((¬(∀x(¬Q(x,x))))→(¬(∀x(∀y(¬Q(x,y)))))))',
          '((¬(∀x(¬Q(x,x))))→(¬(∀x(∀y(¬Q(x,y))))))',
          '((∃xQ(x,x))→(¬(∀x(¬Q(x,x)))))',
          '((∃xQ(x,x))→(¬(∀x(∀y(¬Q(x,y))))))',
          '((¬(∀x(∀y(¬Q(x,y)))))→(∃x(¬(∀y(¬Q(x,y))))))',
          '((¬(∀y(¬Q(x,y))))→(∃y(¬(¬Q(x,y)))))',
          '(((∃y(¬(¬Q(x,y)))))→(∃yQ(x,y)))'
          '((∃x(¬(∀y(¬Q(x,y)))))→(∃x(∃yQ(x,y))))',
          '((∃xQ(x,x))→(∃x(¬(∀y(¬Q(x,y))))))',
          '((∃xQ(x,x))→(∃x(∃yQ(x,y))))']]
##
    E=E+[['├((∀x(Q(x))→R(x))→((∀xQ(x))→(∀xR(x))))',
          '((∀x(Q(x)→R(x)))→(Q(x)→R(x)))',
          '((Q(x)→R(x))→(((∀xQ(x))→Q(x))→((∀xQ(x))→R(x))))',
          '((∀x(Q(x)→R(x)))→(((∀xQ(x))→Q(x))→((∀xQ(x))→R(x))))',
          '(((∀x(Q(x)→R(x)))→(((∀xQ(x))→Q(x))→((∀xQ(x))→R(x))))→(((∀xQ(x))→Q(x))→((∀x(Q(x)→R(x)))→((∀xQ(x))→R(x)))))',
         '(((∀xQ(x))→Q(x))→((∀x(Q(x)→R(x)))→((∀xQ(x))→R(x))))',
          '((∀xQ(x))→Q(x))',
          '((∀x(Q(x)→R(x)))→((∀xQ(x))→R(x)))',
          '(∀x((∀x(Q(x)→R(x)))→((∀xQ(x))→R(x))))',
          '((∀x((∀x(Q(x)→R(x)))→((∀xQ(x))→R(x))))→((∀x(Q(x)→R(x)))→(∀x((∀xQ(x))→R(x)))))',
          '((∀x(Q(x)→R(x)))→(∀x((∀xQ(x))→R(x))))',
          '((∀x((∀xQ(x))→R(x)))→((∀xQ(x))→(∀xR(x))))',
          '((∀x(Q(x))→R(x))→((∀xQ(x))→(∀xR(x))))']]

    E=E+[['├((∀x(Q(x)→R(x)))→((∃xQ(x))→(∃xR(x))))',
          '((∀x(Q(x)→R(x)))→(Q(x)→R(x)))',
          '(R(x)→(∃xR(x)))',
          '((R(x)→(∃xR(x)))→(Q(x)→(R(x)→(∃xR(x)))))',
          '(Q(x)→(R(x)→(∃xR(x))))',
          '((Q(x)→(R(x)→(∃xR(x))))→((Q(x)→R(x))→(Q(x)→(∃xR(x)))))',
          '((Q(x)→R(x))→(Q(x)→(∃xR(x))))',
          '((Q(x)→(∃xR(x)))→((¬(∃xR(x)))→(¬Q(x))))',
          '((Q(x)→R(x))→((¬(∃xR(x)))→(¬Q(x))))',
          '((∀x(Q(x)→R(x)))→((¬(∃xR(x)))→(¬Q(x))))',
          '(∀x((∀x(Q(x)→R(x)))→((¬(∃xR(x)))→(¬Q(x)))))',
          '((∀x((∀x(Q(x)→R(x)))→((¬(∃xR(x)))→(¬Q(x)))))→((∀x(Q(x)→R(x)))→(∀x((¬(∃xR(x)))→(¬Q(x))))))',
          '((∀x(Q(x)→R(x)))→(∀x((¬(∃xR(x)))→(¬Q(x)))))',
          '((∀x((¬(∃xR(x)))→(¬Q(x))))→((¬(∃xR(x)))→(∀x(¬Q(x)))))',
          '(((¬(∃xR(x)))→(∀x(¬Q(x))))→((¬(∀x(¬Q(x))))→(∃xR(x))))',
          '((∀x(Q(x)→R(x)))→((¬(∃xR(x)))→(∀x(¬Q(x)))))',
          '((∀x(Q(x)→R(x)))→((¬(∀x(¬Q(x))))→(∃xR(x))))',
          '((∃xQ(x))→(¬(∀x(¬Q(x)))))',
          '(((∃xQ(x))→(¬(∀x(¬Q(x)))))→(((¬(∀x(¬Q(x))))→(∃xR(x)))→((∃xQ(x))→(∃xR(x)))))',
          '(((¬(∀x(¬Q(x))))→(∃xR(x)))→((∃xQ(x))→(∃xR(x))))',
           '((∀x(Q(x)→R(x)))→((∃xQ(x))→(∃xR(x))))']]
    E=E+[['├(((∀xQ(x))∧(∀xR(x)))→(∀x(Q(x)∧R(x))))',
          '(((∀xQ(x))∧(∀xR(x)))→(∀xQ(x)))',
           '((∀xQ(x))→Q(x))',
          '(((∀xQ(x))∧(∀xR(x)))→Q(x))',
          '(((∀xQ(x))∧(∀xR(x)))→(∀xR(x)))',
          '((∀xR(x))→R(x))',
          '(((∀xQ(x))∧(∀xR(x)))→R(x))',
          '(((∀xQ(x))∧(∀xR(x)))→(Q(x)∧R(x)))',
          '(∀x(((∀xQ(x))∧(∀xR(x)))→(Q(x)∧R(x))))',
          '((∀x(((∀xQ(x))∧(∀xR(x)))→(Q(x)∧R(x))))→(((∀xQ(x))∧(∀xR(x)))→(∀x(Q(x)∧R(x)))))',
          '(((∀xQ(x))∧(∀xR(x)))→(∀x(Q(x)∧R(x))))']]   
    E=E+[['├(((∀xQ(x))∨(∀xR(x)))→(∀x(Q(x)∨R(x))))',
          '((∀xQ(x))→Q(x))',
          '((∀xR(x))→R(x))',
          '(((∀xQ(x))∨(∀xR(x)))→(Q(x)∨R(x)))',
          '(∀x(((∀xQ(x))∨(∀xR(x)))→(Q(x)∨R(x))))',
          '((∀x(((∀xQ(x))∨(∀xR(x)))→(Q(x)∨R(x))))→(((∀xQ(x))∨(∀xR(x)))→(∀x(Q(x)∨R(x)))))',
          '(((∀xQ(x))∨(∀xR(x)))→(∀x(Q(x)∨R(x))))']]
##
    E=E+[['├((∃x(Q(x)∨R(x)))→((∃xQ(x))∨(∃xR(x))))',
          '((∀x(¬Q(x)))→(¬Q(x)))',
          '((∀x(¬R(x)))→(¬R(x)))',
          '(((∀x(¬Q(x)))∧(∀x(¬R(x))))→((¬Q(x))∧(¬R(x))))',
          '(∀x(((∀x(¬Q(x)))∧(∀x(¬R(x))))→((¬Q(x))∧(¬R(x)))))',
          '((∀x(((∀x(¬Q(x)))∧(∀x(¬R(x))))→((¬Q(x))∧(¬R(x)))))→(((∀x(¬Q(x)))∧(∀x(¬R(x))))→(∀x((¬Q(x))∧(¬R(x))))))',
          '(((∀x(¬Q(x)))∧(∀x(¬R(x))))→(∀x((¬Q(x))∧(¬R(x)))))',
          '((((∀x(¬Q(x)))∧(∀x(¬R(x))))→(∀x((¬Q(x))∧(¬R(x)))))→((¬(∀x((¬Q(x))∧(¬R(x)))))→(¬((∀x(¬Q(x)))∧(∀x(¬R(x)))))))',
          '((¬(∀x((¬Q(x))∧(¬R(x)))))→(¬((∀x(¬Q(x)))∧(∀x(¬R(x))))))',
          '((¬(∀x(¬(Q(x)∨R(x)))))→((¬(∀x(¬Q(x))))∨(¬(∀x(¬R(x))))))',
          '((∃x(Q(x)∨R(x)))→((∃xQ(x))∨(∃xR(x))))']]
    E=E+[['├(∀x(P(x)∨(¬P(x))))',
          '((¬P(x))→(¬P(x)))',
          '(((¬P(x))→(¬P(x)))→(P(x)∨(¬P(x))))',
          '(P(x)∨(¬P(x)))',
          '(∀x(P(x)∨(¬P(x))))']]
    E=E+[['├((∃x(∀yQ(x,y)))→(∀y(∃xQ(x,y))))',
          '((∃x(∀yQ(x,y)))→(∀yQ(x,y)))',
          '((∀yQ(x,y))→Q(x,y))',
          '(Q(x,y)→(∃xQ(x,y)))',
          '((∀yQ(x,y))→(∃xQ(x,y)))',
          '(∀y((∀yQ(x,y))→(∃xQ(x,y))))',
          '((∀y((∀yQ(x,y))→(∃xQ(x,y))))→((∀yQ(x,y))→(∀y(∃xQ(x,y)))))',
          '((∀yQ(x,y))→(∀y(∃xQ(x,y))))',
          '((∃x(∀yQ(x,y)))→(∀y(∃xQ(x,y))))']]
##
    E=E+[['├((∃x(Q(x)∧R(x)))→((∃xQ(x))∧(∃xR(x))))',
          '((∀x(¬Q(x)))→(¬Q(x)))',
          '((∀x(¬R(x)))→(¬R(x)))',
          '(((∀x(¬Q(x)))∨(∀x(¬R(x))))→((¬Q(x))∨(¬R(x))))',
          '(∀x(((∀x(¬Q(x)))∨(∀x(¬R(x))))→((¬Q(x))∨(¬R(x)))))',
          '((∀x(((∀x(¬Q(x)))∨(∀x(¬R(x))))→((¬Q(x))∨(¬R(x)))))→(((∀x(¬Q(x)))∨(∀x(¬R(x))))→(∀x((¬Q(x))∨(¬R(x))))))',
          '(((∀x(¬Q(x)))∨(∀x(¬R(x))))→(∀x((¬Q(x))∨(¬R(x)))))',
          '((((∀x(¬Q(x)))∨(∀x(¬R(x))))→(∀x((¬Q(x))∨(¬R(x)))))→((¬(∀x((¬Q(x))∨(¬R(x)))→(¬(∀x(¬Q(x)))∨(∀x(¬R(x))))))))',
          '((¬(∀x((¬Q(x))∨(¬R(x)))→(¬(∀x(¬Q(x)))∨(∀x(¬R(x)))))))'
          
          '∃x(Q(x)∧R(x))→(∃xQ(x)∧∃xR(x))']]
    E=E+[['├((∀xQ(x))↔(¬(∃x(¬Q(x)))))']]
    E=E+[['├((∃xQ(x))↔(¬(∀x(¬Q(x)))))']]
    E=E+[['├((¬(∃xQ(x)))↔(∀x(¬Q(x))))']]
    E=E+[['├((¬(∀xQ(x)))↔(∃x(¬Q(x))))']]
    E=E+[['├((∀xQ(x)→R)↔(∃x(Q(x)→R)))']]
    E=E+[['├((R→∀xQ(x))↔(∀x(R→Q(x))))']]
    E=E+[['├((∃xQ(x)→R)↔(∀x(Q(x)→R)))']]
    E=E+[['├((R→∃xQ(x))↔(∃x(R→Q(x))))']]
    
    E=E+[['├((∀x(P(x)∧Q(x)))→((∀xP(x))∧(∀xQ(x))))',
         '(∀x(P(x)∧Q(x)))','├∀xP(x)∧∀xQ(x)',
          '(∀x(P(x)∧Q(x)))',
          '((∀x(P(x)∧Q(x)))→(P(x)∧Q(x)))',
          '(P(x)∧Q(x))',
          '((P(x)∧Q(x))→P(x))',
          'P(x)',
          '(∀xP(x))',
          '((P(x)∧Q(x))→Q(x))',
          'Q(x)',
          '(∀xQ(x))',
          '((∀xP(x))∧(∀xQ(x)))']]
    return E

def resolutionmethod( ):
    E=[['Q'],['¬R','Q'],['¬Q']]
    E=[['P'], ['P','¬Q'],['¬P','Q'],['P','¬R'], ['¬P','R'], ['¬Q','¬R']]
    E=[['P'],['Q'],['¬R'],['¬P','¬Q','R']]

    return

#哥德尔编码
def GodelCode1(e):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','P','Q','R','S','x','y','c','├',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149, 151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283,293,307,331,337,
       347,349,353,359,367,383,389,397,401,409,421,443,449,457,461,463,467,487,491,499,
       503,509,521,523,541,547,557,563,569,571,577,587,593,599]
    code=1
    k=0
    for a in e:
        i=D.index(a)
        n=P[i]
        code=code*P[k]**n
        k=k+1
    return code

def GodelCodes1(E):
    k=0
    codes=[]
    for e in E:
        code=GodelCode1(e)
        codes=codes+[code]
    return codes

def GodelDecode1(m):
    D=['(',')','→','¬','∧','∨','↔','∀','∃','P','Q','R','S','x','y','c','├',',',' ']
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149, 151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283,293,307,331,337,
       347,349,353,359,367,383,389,397,401,409,421,443,449,457,461,463,467,487,491,499,
       503,509,521,523,541,547,557,563,569,571,577,587,593,599]
    p=0
    C=''
    while m !=1:
        k=0
        while (m%P[p]) == 0:
            m=m//P[p]
            k=k+1
        p=p+1
        i=P.index(k)
        c=D[i]
        C=C+c
    return C

def GodelDecodes1(ms):
    for m in ms:
        s=GodelDecode1(m)
        print("%r"%s)
    return

#无前缀码哥德尔编码
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
    D=['(',')','→','¬','∧','∨','↔','∀','∃','P','Q','R','S','x','y','c','├',',',' ']
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

def validargument( ):
    p=['((not R) | P)','((not P) | (Q&R))', 'R']
    s='Q'
    p=['(P&Q)','((not Q) | R)']
    s='R'
    p=['((not(P&Q))|R)','P']
    s='((not Q)|R)'
    p=['((not Q)| (not R))','((not P) | (Q&R))']
    s='(not P)'
    p=['((not P)|Q)','(not(R&Q))','R']
    s='(not P)'
    p=['(not (P|(not Q)))','((not R)|P)']
    s='((not R)|Q)'
#0
    p=['(P|Q)','((not P)|(not R))','R']
    s='(not Q)'
    p=['((P&Q)|R)','(not P)']
    s='R'
#0
    p=['((not P)|Q)','(Q&R)']
    s='P'
    p=['((P&Q)|R)','(not(P|Q))']
    s='R'
#0
    p=['((not P)|Q)','((not R)|S)','(Q|R)']
    s='(P|S)'
    p=['(P|((not Q)&R))','((not Q)|(not P))']
    s='(not Q)'
#0
    p=['((not Q)|((not Q)|Q))','((not R)|((not Q)|R))','((not Q)|R)']
    s='R'
    p=['((not P)|R)','((not Q)|S)','(P|Q)']
    s='(R|S)'
#0
    p=['((not P)|R)','((not Q)|S)','(R|S)']
    s='(P|Q)'
#0
    p=['((not P)|R)','((not Q)|S)','(R|Q)']
    s='(P|S)'
    truthtable4(p,s)
    return

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
    P=[7, 11, 41, 43, 47, 61, 67, 83, 89, 97, 101,103,107,109,127, 131,137,139,149]
    S=[151, 157,163,167,
       173,179,181,191,193,197,199,211,241,251,257,263,269,271,277,281,283,293,307,331,337,
       347,349,353,359,367,383,389,397,401,409,421,443,449,457,461,463,467,487,491,499,
       503,509,521,523,541,547,557,563,569,571,577,587,593,599]
    E=['((∀x(¬Q(x)))→(¬Q(y)))',
          '(((∀x(¬Q(x)))→(¬Q(y)))→((¬(¬Q(y)))→(¬(∀x(¬Q(x))))))',
          '((¬(¬Q(y)))→(¬(∀x(¬Q(x)))))',
          '(Q(y)→(¬(¬Q(y))))',
          '(Q(y)→(¬(∀x(¬Q(x)))))',
          '((∀xQ(x))→Q(y))',
          '((∀xQ(x))→(¬(∀x(¬Q(x)))))',
          '((∀xQ(x))→(∃xQ(x)))']
    codes=GodelCodes(E)
    return codes

def main3( ):
    E=['¬(∀xQ(x)→∀yQ(y))',
       '¬(∀y(∀xQ(x)→Q(y)))',
       '¬(∀y∃x(Q(x)→Q(y)))',
       '¬(∀y∃x(¬Q(x)∨Q(y)))'
       '∃y∀x(Q(x)∧¬Q(y))',
       '∀x(Q(x)∧¬Q(c))']
    E=['¬(∃xQ(x)→∃yQ(y))',
       '¬(∀x(Q(x)→∃yQ(y)))',
       '¬(∀x∃y(Q(x)→Q(y)))'
       '¬(∀x∃y(¬Q(x)∨Q(y)))'
       '∃x∀y(Q(x)∧¬Q(y))',
       '∀y(Q(c)∧¬Q(y))']
    E=['¬(∀xQ(x)→∃xQ(x))'
       '¬(∀xQ(x)→∃yQ(y))',
       '¬(∃x(Q(x)→∃yQ(y)))',
       '¬(∃x∃y(Q(x)→Q(y)))',
       '¬(∃x∃y(¬Q(x)∨Q(y)))'
       '∀x∀y(Q(x)∧¬Q(y))']
    E=['¬(Q(c)→∃xQ(x))',
       '¬(∃x(Q(c)→Q(x)))',
       '¬(∃x(¬Q(c)∨Q(x)))',
       '∀x(Q(c)∧¬Q(x))']
    E=['¬(∀x∀yQ(x,y)→∀y∀xQ(x,y))'
       '¬(∀x0∀y0Q(x0,y0)→∀y1∀x1Q(x1,y1))',
       '¬(∀y1∀x1(∀x0∀y0Q(x0,y0)→Q(x1,y1)))',
       '¬(∀y1∀x1∃x0∃y0(Q(x0,y0)→Q(x1,y1)))',
       '¬(∀y1∀x1∃x0∃y0(¬Q(x0,y0)∨Q(x1,y1)))'
       '∃y1∃x1∀x0∀y0(Q(x0,y0)∧¬Q(x1,y1))',
       '∀x0∀y0(Q(x0,y0)∧¬Q(c1,c0))']
    E=[ '¬(∃x∃yQ(x,y)→∃y∃xQ(x,y))',
        '¬(∃x0∃y0Q(x0,y0)→∃y1∃x1Q(x1,y1))',
        '¬(∀y0∀x0(Q(x0,y0)→∃x1∃y0Q(x1,y1)))',
        '¬(∀y0∀x0∃x1∃y1(Q(x0,y0)→Q(x1,y1)))',
        '¬(∀y0∀x0∃x1∃y1(¬Q(x0,y0)∨Q(x1,y1)))',
        '∃x0∃y0∀x1∀y1(Q(x0,y0)∧¬Q(x1,y1)))',
        '∀x1∀y1(Q(c0,c1)∧¬Q(x1,y1)))']
    E=['¬∀x∀yQ(x,y)→∀xQ(x,x)',
       '¬(∀x0∀y0Q(x0,y0)→∀x1Q(x1,x1))',
       '¬∀x1(∀x0∀y0Q(x0,y0)→Q(x1,x1))',
       '¬∀x1∃x0∃y0(Q(x0,y0)→Q(x1,x1))',
       '∃x1∀x0∀y0(¬Q(x0,y0)∨Q(x1,x1))',
       '∃x1∀x0∀y0(Q(x0,y0)∧¬Q(x1,x1))',
       '∀x0∀y0(Q(x0,y0)∧¬Q(c0,c0))']
    E=['¬((∃xQ(x,x))→(∃x(∃yQ(x,y))))',
       '¬(∃x0Q(x0,x0)→∃x1∃y1Q(x1,y1))',
       '¬∀x0(Q(x0,x0)→∃x1∃y1Q(x1,y1))',
       '¬∀x0∃x1∃y1(Q(x0,x0)→Q(x1,y1))',
       '¬∀x0∃x1∃y1(¬Q(x0,x0)∨Q(x1,y1))',
       '∃x0∀x1∀y1(Q(x0,x0)∧¬Q(x1,y1))',
       '∀x1∀y1(Q(c0,c0)∧¬Q(x1,y1))']
    E=['¬((∀x(Q(x))→R(x))→((∀xQ(x))→(∀xR(x))))',
       '¬(∀x0(Q(x0)→R(x0))→(∀x1Q(x1)→∀x2R(x2)))',
       '¬(∀x0(Q(x0)→R(x0))→∃x1(Q(x1)→∀x2R(x2)))',
       '¬(∀x0(Q(x0)→R(x0))→∃x1∀x2(Q(x1)→R(x2)))',
       '¬∃x0((Q(x0)→R(x0))→∃x1∀x2(Q(x1)→R(x2)))',
       '¬∃x0∃x1∀x2((Q(x0)→R(x0))→(Q(x1)→R(x2)))',
       '¬∃x0∃x1∀x2(¬(¬Q(x0)∨R(x0))∨(¬Q(x1)∨R(x2)))',
       '∀x0∀x1∃x2((¬Q(x0)∨R(x0))∧(Q(x1)∧¬R(x2)))',
       '∀x0∀x1((¬Q(x0)∨R(x0))∧(Q(x1)∧¬R(f(x0,x1))))']
#
    E=['¬(∀x(Q(x)∨R(x))→(∀xQ(x)∨∀xR(x)))',
       '¬(∀x(Q(x)∨R(x))→(∀x0Q(x0)∨∀x1R(x1)))',
       '¬(∀x(Q(x)∨R(x))→∀x0∀x1(Q(x0)∨R(x1)))',
       '¬∀x0∀x1(∀x(Q(x)∨R(x))→(Q(x0)∨R(x1)))',
       '¬∀x0∀x1∃x((Q(x)∨R(x))→(Q(x0)∨R(x1)))',
       '∃x0∃x1∀x((¬Q(x)∧¬R(x))∨(Q(x0)∨R(x1)))',
       '∀x((¬Q(x)∧¬R(x))∨(Q(c0)∨R(c1)))']
    E=['¬((∀x(Q(x)→R(x)))→((∃xQ(x))→(∃xR(x))))',      
    '¬(((∀xQ(x))∧(∀xR(x)))→(∀x(Q(x)∧R(x))))',
    '¬(((∀xQ(x))∨(∀xR(x)))→(∀x(Q(x)∨R(x))))',
    '¬((∃x(Q(x)∨R(x)))→((∃xQ(x))∨(∃xR(x))))',
    '¬(∀x(P(x)∨(¬P(x))))',
    '¬∃x∀yQ(x,y)→∀y∃xQ(x,y)']
    return


