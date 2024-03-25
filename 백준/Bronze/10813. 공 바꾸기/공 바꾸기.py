a,b=map(int,input().split())
l=[0]*a
for t in range(a):
    l[t]=t+1
for _ in range(b):
    i,j=map(int,input().split())
    l[i-1],l[j-1]=l[j-1],l[i-1]
print(*l)