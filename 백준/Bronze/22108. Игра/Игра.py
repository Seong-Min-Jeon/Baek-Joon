import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    a=int(ip())
    l=[[] for _ in range(a)]
    b=0
    for i in range(a):
        l[i]=list(map(int,ip().split()))
        if(0 in l[i]): b=1
    if(b==1): print('YES'); continue
    for e in l:
        for i in range(1,len(e)):
            if(e[i]==e[i-1]): b=1; break
        if(b==1): break
    if(b==1): print('YES'); continue
    t=[]
    for e in l:
        if(len(t)==0): t=e; continue
        for i in range(len(e)):
            if(t[i]==e[i]): b=1; break
        if(b==1): print('YES'); break
        t=e        
    if(b==1): continue
    print('NO')