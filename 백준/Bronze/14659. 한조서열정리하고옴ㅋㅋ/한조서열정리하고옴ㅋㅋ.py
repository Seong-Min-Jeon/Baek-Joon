I=input
I()
l=list(map(int,I().split()))
n,m,c=0,0,0
for e in l:
    if(e>n): c=0; n=e
    else: c+=1; m=max(m,c)
print(m)