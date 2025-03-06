import sys
I=sys.stdin.readline
for _ in range(3):
    s=0
    for _ in range(int(I())):
        s+=int(I())
    if(s==0): print(0)
    elif(s<0): print('-')
    else: print('+')