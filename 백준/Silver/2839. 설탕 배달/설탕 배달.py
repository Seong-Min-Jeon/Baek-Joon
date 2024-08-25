a=int(input())
m=float('inf')
for i in range(a//5+1):
    for j in range(a//3+1):
        if(i*5+j*3==a):
            m=min(m,i+j)        
if(m==float('inf')): print(-1)
else: print(m)