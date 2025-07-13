import math
x,y=map(int,input().split())
l=[1 if math.gcd(i,y)==1 else 0 for i in range(y)]
for i in range(y-1,1,-1):
    for j in range(i+1,y):
        if(math.gcd(i,j)==1 and l[j]==0): l[i]=1; break
if(l[x]==1): print('khj20006')
else: print('putdata')