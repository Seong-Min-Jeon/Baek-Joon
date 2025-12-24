n,k=map(int,input().split())
l=[1e9]*(n+1)
l[0]=0
for i in range(n):
    if(i+1<=n): l[i+1]=min(l[i+1],l[i]+1)
    if(i+i//2<=n): l[i+i//2]=min(l[i+i//2],l[i]+1)
if(l[-1]<=k): print('minigimbob')
else: print('water')