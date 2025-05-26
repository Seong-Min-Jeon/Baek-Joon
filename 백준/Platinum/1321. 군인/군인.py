import sys
I=sys.stdin.readline
def init(l,r,i):
    if(l==r): t[i]=d[l]; return t[i]
    m=(l+r)//2
    t[i]=init(l,m,i*2)+init(m+1,r,i*2+1)
    return t[i]
def query(s,e,i,v):
    if(s==e): return s+1
    m=(s+e)//2
    if(t[i*2]<v):
        return query(m+1,e,i*2+1,v-t[i*2])
    elif(t[i*2]==v):
        return m+1
    else:
        return query(s,m,i*2,v)
def update(s,e,p,i,v):
    if(i<s or i>e): return t[p]
    t[p]+=v
    if(s!=e):
        m=(s+e)//2
        update(s,m,p*2,i,v)
        update(m+1,e,p*2+1,i,v)
n=int(I())
d=list(map(int,I().split()))
t=[0]*(len(d)*4)
init(0,len(d)-1,1)
for _ in range(int(I())):
    s=I().strip()
    if(s[0]=='1'):
        a,b,c=map(int,s.split())
        update(0,len(d)-1,1,b-1,c)
    else:
        a,b=map(int,s.split())
        print(query(0,len(d)-1,1,b))