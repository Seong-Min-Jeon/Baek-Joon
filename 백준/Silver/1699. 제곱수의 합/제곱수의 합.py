n=int(input())
l=[1e9 for _ in range(n+1)]
l[0]=0
for i in range(n+1):
    for j in range(int(i**0.5)+1):
        l[i]=min(l[i],l[i-j**2]+1)
print(l[-1])