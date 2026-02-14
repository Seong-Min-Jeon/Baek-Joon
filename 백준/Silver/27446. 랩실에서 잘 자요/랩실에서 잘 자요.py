n,m=map(int,input().split())
s=set([i+1 for i in range(n)])
for e in map(int,input().split()):
    if(e in s): s.remove(e)
if(len(s)==0): print(0); exit()
l=sorted(list(s))
r=0
t=[]
for e in l:
    if(len(t)==0): t.append(e); continue
    if(e-t[-1]<4): t.append(e)
    else:
        r+=5+2*(t[-1]-t[0]+1)
        t=[e]
r+=5+2*(t[-1]-t[0]+1)
print(r)