i=input
a=int(i()); b=int(i())
c,s=9999,0
l=False
for i in range(a,b+1):
    if(i==1): l=True
    for j in range(2,i):
        if(i%j==0): l=True; break
    if(l==False):
        s+=i
        if(c>i): c=i
    l=False
if(s==0): print(-1); exit()
print(s); print(c)