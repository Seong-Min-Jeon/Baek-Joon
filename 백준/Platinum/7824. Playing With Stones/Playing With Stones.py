import sys
I=sys.stdin.readline
for _ in range(int(I())):
    I()
    x=0
    for e in map(int,I().split()):
        while e%2==1:
            e=(e-1)//2
        x^=e//2
    print('YES' if x else 'NO')