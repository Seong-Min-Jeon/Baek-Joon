n=int(input())
l=[int(input()) for _ in range(n)]
t=0
for i in range(n):
    t=l[i]-t
r=t//2
print(r)
for i in range(n-1):
    l[i]-=r
    r=l[i]
    print(l[i])