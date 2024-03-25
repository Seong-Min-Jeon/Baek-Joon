a,b=map(int,input().split())
l=[0]*a
for _ in range(b):
    i,j,k=map(int,input().split())
    l[i-1:j]=[k]*(j-i+1)    
print(*l)