import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(input())
    if(len(str(n))<len(str(n*2))):
        t=int('5'+'0'*(len(str(n))-1))
        print(t*(int('9'*len(str(n)))-t))
    else:
        print(n*(int('9'*len(str(n)))-n))