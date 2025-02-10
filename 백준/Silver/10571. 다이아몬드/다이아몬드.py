import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    l=[list(map(float,I().split())) for _ in range(n)]
    m=[1 for _ in range(n)]
    for i in range(n):        
        for j in range(i):
            if(l[i][0]>l[j][0] and l[i][1]<l[j][1]):
                m[i]=max(m[i],m[j]+1)
    print(max(m))