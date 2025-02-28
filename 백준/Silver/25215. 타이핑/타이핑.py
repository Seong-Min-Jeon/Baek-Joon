from collections import deque
s=input().strip()
q=deque([])
if(s[0].isupper()): q.append((2,1,1)); q.append((2,1,0))
else: q.append((1,1,0))
v=set()
m=1e9
while q:
    l,i,c=q.popleft()
    if(i==len(s)): m=min(m,l); continue
    if((s[i].isupper() and c==0) or (s[i].islower() and c==1)):
        if(l+2>m): continue
        if((l+2,i+1,1) not in v): v.add((l+2,i+1,1)); q.append((l+2,i+1,1))
        if((l+2,i+1,0) not in v): v.add((l+2,i+1,0)); q.append((l+2,i+1,0))
    else:
        if(l+1>m): continue
        if((l+1,i+1,c) not in v): v.add((l+1,i+1,c)); q.appendleft((l+1,i+1,c))
print(m)