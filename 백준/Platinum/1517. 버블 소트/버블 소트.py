import sys
I=sys.stdin.readline
def query(s,e,i,l,r):
    if(l>e or r<s): return 0
    elif(l<=s and r>=e): return t[i]
    m=(s+e)//2
    return query(s,m,i*2,l,r)+query(m+1,e,i*2+1,l,r)
def update(s,e,p,i,v):
    if(i<s or i>e): return t[p]
    t[p]+=v
    if(s!=e):
        m=(s+e)//2
        update(s,m,p*2,i,v)
        update(m+1,e,p*2+1,i,v)
n=int(I())
d=[(e,i) for i,e in enumerate(list(map(int,I().split())))]
d.sort()
t=[0]*(len(d)*4)
s=0
for e,i in d:
    s+=query(0,len(d)-1,1,i,len(d)-1)
    update(0,len(d)-1,1,i,1)
print(s)