import sys
ip=sys.stdin.readline
while True:
    a,b,c=sorted(list(map(int,ip().split())))
    if(a==0): break
    if(a**2+b**2==c**2): print('right')
    else: print('wrong')