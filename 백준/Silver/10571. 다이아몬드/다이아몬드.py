import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    l=[tuple(map(float,I().split())) for _ in range(n)]
    m=[0 for _ in range(n)]
    for i in range(n):
        m[i]=1
        for j in range(i):
            if(l[i][0]>l[j][0] and l[i][1]<l[j][1]):
                m[i]=max(m[i],m[j]+1)
    print(max(m))