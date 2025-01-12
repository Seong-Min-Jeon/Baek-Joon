a=int(input())
if(a==0): print('NO'); exit()
v=2432902008176640000
for i in range(20,0,-1):
    v//=i
    if(a>=v): a-=v
if(a==0): print('YES')
else: print('NO')