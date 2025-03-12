from bisect import bisect_left as b
a=int(input())
l=list(map(int,input().split()))
n=[]
m=[]
for e in l:
    i=b(m,e)
    if(i>=len(m)): m.append(e)
    else: m[i]=e
    n.append(i)
i=len(m)
print(i)
r=[]
for j,e in enumerate(reversed(n)):    
    if(e==i-1): r.append(l[a-j-1]); i-=1
print(*reversed(r))