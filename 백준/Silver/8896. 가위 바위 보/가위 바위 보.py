import sys
I=sys.stdin.readline
for _ in range(int(I())):
    l=[I().strip() for _ in range(int(I()))]
    s=set()
    z=1
    for i in range(len(l[0])):
        r=[]
        for j in range(len(l)):
            if(j in s): r.append(0); continue
            r.append(l[j][i])
        if((0 in r and len(set(r))==3) or (0 not in r and len(set(r))==2)):
            if('S' not in r):
                for k in range(len(r)):
                    if(r[k]=='R'): s.add(k)
            elif('P' not in r):
                for k in range(len(r)):
                    if(r[k]=='S'): s.add(k)
            elif('R' not in r):
                for k in range(len(r)):
                    if(r[k]=='P'): s.add(k)
        if(len(l)-len(s)==1):
            print((set(i for i in range(len(l)))-set(s)).pop()+1)
            z=0
            break
    if(z): print(0)