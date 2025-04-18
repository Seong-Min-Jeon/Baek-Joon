l=[0]*9999
l[0],l[1]=1,1
r=set()
for i in range(9999):
    if(l[i]==1): continue
    r.add(i)
    for j in range(2*i,9999,i):
        l[j]=1
for _ in range(int(input())):
    n=int(input())
    d=1e9
    x=0
    for e in r:
        if(n-e in r and d>abs((n-e)-e)):
            d=abs((n-e)-e)
            x=e
    print(min(x,n-x),max(x,n-x))