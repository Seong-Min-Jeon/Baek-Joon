def f(i,j,p):
    if(i==0 and j==0):
        s.add(p)
        return
    if(i>0):
        t=(p+b)%M
        f(i-1,j,t)
    if(i<j and j>0):
        t=(p*c)%M
        f(i,j-1,t)
M=10**5
n,a,b,c=map(int,input().split())
d=[]
s=set()
f(n,n,a)
print(max(s))