x,n=map(int,input().split())
for _ in range(n):
    if(x%2): x=(2*x)^6
    else: x=(x//2)^6
print(x)