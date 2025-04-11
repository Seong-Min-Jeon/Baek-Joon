def f(n,r):
    global c
    if(n==r): return
    if(len(t[n])==0 or (len(t[n])==1 and t[n][0]==r)): c+=1; return
    for p in t[n]: f(p,r)
n=int(input())
l=list(map(int,input().split()))
t=[[] for _ in range(n)]
s=0
for i,e in enumerate(l):
    if(e==-1): s=i; continue
    t[e].append(i)
r=int(input())
c=0
f(s,r)
print(c)