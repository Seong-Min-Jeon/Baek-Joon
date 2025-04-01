for _ in range(int(input())):
    l=input().strip().split(',')
    d={}
    for e in l:
        t=e.split(':')
        d[t[0]]=t[1]
    m=input().strip().split('|')
    y=10**4
    for e in m:
        t=e.split('&')
        x=0
        for k in t:
            x=max(x,int(d[k]))
        y=min(y,x)
    print(y)