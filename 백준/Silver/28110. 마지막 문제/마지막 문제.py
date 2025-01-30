n=int(input())
l=list(map(int,input().split()))
l.sort()
m,d=0,0
for i in range(n-1):
    t=(l[i+1]+l[i])//2
    if(d<t-l[i]): d=t-l[i]; m=t
if(d==0): print(-1)
else: print(m)