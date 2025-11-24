I=input
d={}
for _ in range(int(I())):
    s=input().split(' = ')
    d[s[0]]=s[1]
for _ in range(int(I())):
    I()
    r=[]
    for e in I().strip().split():
        r.append(d.get(e,e))
    print(*r)