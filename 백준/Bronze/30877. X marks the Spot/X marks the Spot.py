import sys
i=sys.stdin.readline
for _ in range(int(i())):
    a,b=i().split()
    m=a.find('x')
    if(m==-1): m=a.find('X')
    print(b[m].upper(), end='')