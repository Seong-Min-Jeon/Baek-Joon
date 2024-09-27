a,b=map(int,input().split())
for i in range(a,b+1):
    if(i==1): continue
    p=1
    for j in range(2,int(i**0.5)+1):
        if(i%j==0): p=0; break
    if(p==1): print(i)