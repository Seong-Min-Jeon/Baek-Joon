import sys
I=sys.stdin.readline
for _ in range(int(I())):
    j,n=map(int,I().split())
    l=[]
    for _ in range(n):
        r,c=map(int,I().split())
        l.append(r*c)
    l.sort(reverse=True)
    for i in range(n):
        j-=l[i]
        if(j<=0): break
    print(i+1)