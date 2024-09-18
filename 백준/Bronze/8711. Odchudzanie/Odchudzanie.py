input()
m,n=0,0
for e in map(int,input().split()):
    if(m<e): m=e; continue
    n=max(n,m-e)
print(n)