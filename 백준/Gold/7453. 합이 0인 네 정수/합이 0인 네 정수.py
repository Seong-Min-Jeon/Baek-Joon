import sys
def fuc():
    ip = sys.stdin.readline
    n=int(ip())
    a,b,c,d=[],[],[],[]
    for _ in range(n):
        p,q,r,s = map(int,ip().split())
        a.append(p)
        b.append(q)
        c.append(r)
        d.append(s)
    t=dict()
    for i in a:
        for j in b:
            v=i+j
            if(v in t):
                t[v]+=1
            else:
                t[v]=1
    r=0
    for i in c:
        for j in d:
            v=-i-j
            if(v in t):
                r+=t[v]
    return r
print(fuc())