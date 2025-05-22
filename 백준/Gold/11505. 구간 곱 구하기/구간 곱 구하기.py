import sys
I=sys.stdin.readline
M=1000000007
def init(l,r,i):
    if(l==r): t[i]=d[l]; return t[i]
    m=(l+r)//2
    t[i]=(init(l,m,i*2)*init(m+1,r,i*2+1))%M
    return t[i]
def query(s,e,i,l,r):
    if(l>e or r<s): return 1
    elif(l<=s and r>=e): return t[i]
    m=(s+e)//2
    return (query(s,m,i*2,l,r)*query(m+1,e,i*2+1,l,r))%M
def update(s,e,p,i,v,w):
    if(i<s or i>e): return t[p]
    t[p]=((t[p]*pow(w,M-2,M))%M*v)%M
    if(s!=e):
        m=(s+e)//2
        update(s,m,p*2,i,v,w)
        update(m+1,e,p*2+1,i,v,w)
n,m,k=map(int,I().split())
d=[int(I()) for _ in range(n)]
t=[0]*(len(d)*4)
init(0,len(d)-1,1)
z=set()
for _ in range(m+k):
    a,b,c=map(int,I().split())
    if(a==1 and c==0): 
        update(0,len(d)-1,1,b-1,1,d[b-1]); d[b-1]=1; z.add(b)
    elif(a==1):
        update(0,len(d)-1,1,b-1,c,d[b-1]); d[b-1]=c
        if(b in z): z.remove(b)
    if(a==2):
        if(len(z)>0 and (min(z)>=b or b>=max(z))): print(0)
        else: print(query(0,len(d)-1,1,b-1,c-1))