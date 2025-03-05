def f(n,s,d,r):
    while True:
        n,s,d,r=g(n,s,d,r)
        if(s==1 and 1<d<=l[n-2]+1): n,s,d,r=n,s+1,d,r+'L'
        elif(s==1 and l[n-2]+1<d): n,s,d,r=n,s+l[n-2]+1,d,r+'R'
        else: return r
def g(n,s,d,r):
    while True:
        if(1<s<=l[n-2]+1 and 1<d<=l[n-2]+1): n,s,d,r=n-2,s-1,d-1,r
        elif(l[n-2]+1<s and l[n-2]+1<d): n,s,d,r=n-1,s-l[n-2]-1,d-l[n-2]-1,r
        else: return (n,s,d,r)
l=[1,1]
for _ in range(49): l.append(l[-2]+l[-1]+1)
n,s,d=map(int,input().split())
r=''
n,s,d,r=g(n,s,d,r)
r='U'*len(f(n,1,s,''))
print(f(n,1,d,r))