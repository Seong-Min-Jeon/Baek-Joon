a=int(input())
l=list(map(int,input().split()))
b=int(input())
m=0
for i in range(b):
    c,d=list(map(int,input().split()))
    s=0
    for j in range(c):
        s+=l[j]
    if(s>d):
        print(-1)
        exit(0)
    m=max(m,s)
print(2*m)