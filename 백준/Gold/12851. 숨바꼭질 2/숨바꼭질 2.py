n,k=map(int,input().split())
v=[0 for _ in range(10**5+1)]
q=[n]
l=10**5
r=0
while q:
    c=q.pop(0)
    if(v[c]>l): break
    if(c==k): l=v[c]; r+=1
    for e in (c+1, c-1, 2*c):
        if(e<0 or e>10**5): continue
        if(v[e]==0 or v[e]==v[c]+1): q.append(e); v[e]=v[c]+1
print(v[k])
print(r)