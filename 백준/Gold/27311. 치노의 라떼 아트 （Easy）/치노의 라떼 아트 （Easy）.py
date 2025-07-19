import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n,m=map(int,I().split())
    l=[list(I().strip()) for _ in range(n)]
    f=0
    t=[[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(l[i][j]=='#'):
                t[i].append(j)
    for e in t:
        if(len(e)==0): continue
        if(max(e)-min(e)+1!=len(e)): f=1
    if(f): print(0); continue
    a,b=[],[]
    x,y=0,0
    c=0
    for e in t:
        if(c and len(e)!=0): f=1; break
        if(len(e)==0 and len(a)!=0 and len(b)==0): f=1; continue
        elif(len(e)==0 and len(a)!=0 and len(b)!=0): c=1; continue
        elif(len(e)==0): continue
        if(len(a)==0): a=e; x+=1
        elif(e==a and len(b)!=0): f=1
        elif(e==a): x+=1
        elif(e==b): y+=1
        elif(e!=a and len(b)==0):
            if(min(a)==min(e) or max(a)==max(e)): b=e; y+=1
            else: f=1
        elif(e!=a and e!=b): f=1
    if(len(b)==0): f=1
    if(f): print(0); continue
    if(max(len(a),len(b))!=x+y): f=1
    elif(len(a)<=len(b) and abs(len(a)-len(b))!=x): f=1
    elif(len(b)<=len(a) and abs(len(a)-len(b))!=y): f=1
    if(f): print(0)
    else: print(1)