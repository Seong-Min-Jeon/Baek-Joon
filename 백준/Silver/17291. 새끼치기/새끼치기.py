a=int(input())
d={}
s=0
for i in range(1, a+1):
    if(i==1):
        d[1]=1
        continue
    d[i]=0    
    for e in d:
        if(e==i): break
        d[i]+=d.get(e)
    if(i%2==0 and i>4):
        del d[i-4]
    if(i%2==0 and i>3):
        del d[i-3]    
for e in d:
    s+=d.get(e)
print(s)