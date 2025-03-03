import sys
I=sys.stdin.readline
while True:
    b=I().strip()
    if(b=='0'): break
    n,s,t=map(int,b.split())
    l=[]
    while len(l)!=n: 
        l.extend(list(map(int,I().split())))
    r=[[-10**4 for _ in range(n)] for _ in range(t-1)]
    for i in range(t-1):
        for j in range(n):
            if(j<i or j>=(i+1)*s): continue
            m=-10**4
            for k in range(j-s,j):
                if(k<0): continue
                m=max(m,r[i-1][k])
            if(i==0): m=0
            r[i][j]=m+l[j]
    print(max(r[-1][n-s:]))