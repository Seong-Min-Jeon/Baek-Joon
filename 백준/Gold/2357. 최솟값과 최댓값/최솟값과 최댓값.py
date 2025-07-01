import sys
I=sys.stdin.readline
def init1(l,r,i):
    if(l==r): t[i]=d[l]; return t[i]
    m=(l+r)//2
    t[i]=min(init1(l,m,i*2),init1(m+1,r,i*2+1))
    return t[i]
def init2(l,r,i):
    if(l==r): u[i]=d[l]; return u[i]
    m=(l+r)//2
    u[i]=max(init2(l,m,i*2),init2(m+1,r,i*2+1))
    return u[i]
def query1(s,e,i,l,r):
    if(l>e or r<s): return 1e10
    elif(l<=s and r>=e): return t[i]
    m=(s+e)//2
    return min(query1(s,m,i*2,l,r),query1(m+1,e,i*2+1,l,r))
def query2(s,e,i,l,r):
    if(l>e or r<s): return 0
    elif(l<=s and r>=e): return u[i]
    m=(s+e)//2
    return max(query2(s,m,i*2,l,r),query2(m+1,e,i*2+1,l,r))
n,m=map(int,I().split())
d=[int(I()) for _ in range(n)]
t=[1e10]*(len(d)*4)
u=[0]*(len(d)*4)
init1(0,len(d)-1,1)
init2(0,len(d)-1,1)
for _ in range(m):
    a,b=map(int,I().split())
    print(query1(0,len(d)-1,1,a-1,b-1),query2(0,len(d)-1,1,a-1,b-1))