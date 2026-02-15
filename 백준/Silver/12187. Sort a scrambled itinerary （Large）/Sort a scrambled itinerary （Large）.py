import sys
I=sys.stdin.readline
for i in range(int(I())):
    n=int(I())
    d={}
    t=set()
    for _ in range(n):
        k=I().strip()
        v=I().strip()
        d[k]=v
        t.add(k)
        t.add(v)    
    for k in d:
        if(d[k]in t): t.remove(d[k])
    s=t.pop()
    r=''
    for _ in range(n):
        r+=s+'-'+d[s]+' '
        s=d[s]
    print(f'Case #{i+1}: {r[:-1]}')