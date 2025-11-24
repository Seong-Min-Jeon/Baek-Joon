import sys
I=sys.stdin.readline
for k in range(int(I())):
    f=0
    for _ in range(int(I())):
        s=input().strip()
        if('00' in s): f=1
    print(f'Case {k+1}: {'Fallen' if f else 'Standing'}')