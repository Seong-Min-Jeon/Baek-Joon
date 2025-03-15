import sys
I=sys.stdin.readline
def f(l,n):
    if(n==1): return l.pop()
    n//=2
    return sorted([f([l[i][:n] for i in range(n)],n),f([l[i][:n] for i in range(n,2*n)],n),
                   f([l[i][n:] for i in range(n)],n),f([l[i][n:] for i in range(n,2*n)],n)]).pop(1)
n=int(I())
l=[list(map(int,I().split())) for _ in range(n)]
print(*f(l,n))