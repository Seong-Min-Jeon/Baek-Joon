l=[tuple(map(float,input().split())) for _ in range(int(input()))]
for _ in range(int(input())):
    m=int(input())
    v=list(map(int,input().split()))
    n=v[0]
    d=0
    for i in range(1,m):
        d+=((l[n][0]-l[v[i]][0])**2+(l[n][1]-l[v[i]][1])**2)**0.5
        n=v[i]
    print(round(d))