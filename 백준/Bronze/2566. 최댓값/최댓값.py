l=[0,0,0]
for i in range(9):    
    a=list(map(int,input().split()))
    b=max(a)
    if(l[0]<b):    
        l[0]=b
        l[1]=i
        l[2]=a.index(b)
print(f'{l[0]}\n{l[1]+1} {l[2]+1}')