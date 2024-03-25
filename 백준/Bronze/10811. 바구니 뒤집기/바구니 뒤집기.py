a,b=map(int,input().split())
l=[0]*a
for k in range(a):
    l[k]=k+1
for _ in range(b):
    i,j=map(int,input().split())
    l[i-1:j]=list(reversed(l[i-1:j]))    
print(*l)