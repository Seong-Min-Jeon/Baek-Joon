l,u=map(int,input().split())
M=10**9+7
c=0
for i in range(l,u+1):
    c=(c+pow(26,(i-1)//2,M))%M
if(l!=2 and u!=1): print('A')
else: print('H')
print(c)