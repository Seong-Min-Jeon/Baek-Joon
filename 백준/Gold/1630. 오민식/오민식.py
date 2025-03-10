n=int(input())
l=[1 for _ in range(n+1)]
l[0],l[1]=0,0
for i in range(2,n+1):
    if(not l[i]): continue
    for j in range(2*i,n+1,i):
        l[j]=0
s=1
for k in range(n+1):
    if(not l[k]): continue
    for i in range(21):
        if(n<k**i): break    
    s=(s*k**(i-1))%987654321
print(s)