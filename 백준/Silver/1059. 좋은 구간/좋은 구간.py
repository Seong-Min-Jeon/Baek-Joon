n=int(input())
l=[*map(int,input().split())]
k=int(input())
x,y=1,1e9
for e in l:
    if(e<=k): x=max(e+1,x)
    elif(e>=k): y=min(e-1,y)
c=0
for i in range(x,k+1):
    c+=y-2*i+x+1
print(max(0,c-1))