x=int(input())
n=int(input())
d={}
for _ in range(n):
    a,b=input().strip().split()
    if(int(b)<x*0.05): continue
    d[a]=int(b)
l=[]
r={}
for k in d:
    l+=[(d[k]/i,k) for i in range(1,15)]
    r[k]=0
l.sort(reverse=True)
for i in range(14):
    r[l[i][1]]=r[l[i][1]]+1
p=[]
for k in r:
    p.append((k,r[k]))
p.sort()
for e in p:
    print(*e)