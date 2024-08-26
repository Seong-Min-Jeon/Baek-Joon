a=int(input())
l=[0]*1001
l[1]=1; l[2]=0; l[3]=1; l[4]=1; 
for i in range(5, 1001):
    if(l[i-1]!=1): l[i]=1
    if(l[i-3]!=1): l[i]=1
    if(l[i-4]!=1): l[i]=1
print('SK' if l[a]==1 else 'CY')