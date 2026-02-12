import sys
I=sys.stdin.readline
while True:
    t=input().strip()
    if(t=='0'): break
    l=[*map(int,t.split())]
    k=l.pop(0)
    g=[]
    for i in range(10001):
        s=set()
        for e in l:
            if(i>=e): s.add(g[i-e])
        for j in range(1000):
            if(j not in s):
                g.append(j)
                break
    m=int(I())
    r=''    
    for _ in range(m):
        x=0
        t=[*map(int,I().split())]
        for e in t[1:]:
            x^=g[e]
        if(x): r+='W'
        else: r+='L'
    print(r)