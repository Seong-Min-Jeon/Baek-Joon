l,r=[0],[0]
for i in range(1,121): l.append(l[-1]+i)
for e in l: r.append(r[-1]+e)
r.pop(0); r.pop(0)
t=[]
for i in range(int(input())+1):
    if(i in r): t.append(1); continue
    m=1e9
    for v in r:
        if(v<=i): m=min(m,t[i-v]+1)
    t.append(m)
print(t[-1])