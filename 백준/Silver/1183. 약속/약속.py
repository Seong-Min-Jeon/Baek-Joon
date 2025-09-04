I=input
l=[]
for _ in range(int(I())):
    a,b=map(int,I().split())
    l.append(a-b)
l.sort()
while len(l)>2: l.pop(0); l.pop()
if(len(l)==1): print(1)
else: print(l[1]-l[0]+1)