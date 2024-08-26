a=int(input())
l=[0]*1001
l[1]=0; l[2]=1; l[3]=0; l[4]=1
for i in range(5, 1001):
    if(l[i-1]==0): l[i]=1
    if(l[i-3]==0): l[i]=1
    if(l[i-4]==0): l[i]=1
print('SK' if l[a]==1 else 'CY')