a,b,c=map(int,input().split())
p,q=[],[]
i=2
while a>1:
    if(a%i==0):
        p.append(i)
        a//=i
        continue
    i+=1
    if(i>c): break
i=2
while b>1:
    if(b%i==0):
        q.append(i)
        b//=i
        continue
    i+=1
    if(i>c): break
if(len(p)>len(q)): print('First')
else: print('Second')