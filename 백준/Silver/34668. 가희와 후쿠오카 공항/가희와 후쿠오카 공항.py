import sys,math
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())+1
    m=(math.ceil(n/50)-1)*12+6
    h=m//60
    m-=60*h
    print(f'0{6+h}:{str(m).rjust(2,'0')}')