n,m=map(int,input().split())
s=input().strip()
t=sorted(list(s))
a={}
for i in range(m):
    if(t[i] in a): a[t[i]]+=1
    else: a[t[i]]=1
r=''
for e in s:
    if(e in a and a[e]>0): a[e]-=1
    else: r+=e
print(r)