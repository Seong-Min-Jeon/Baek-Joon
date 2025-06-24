import sys
I=sys.stdin.readline
for i in range(int(I())):
    if(i!=0): print()
    n,s,d=map(int,I().split())
    t=s*d
    c=0
    for _ in range(n):
        a,b=map(int,I().split())
        if(a<=t): c+=b
    print(f'Data Set {i+1}:')
    print(c)