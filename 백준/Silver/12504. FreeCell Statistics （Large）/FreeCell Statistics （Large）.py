import sys,math
I=sys.stdin.readline
for i in range(int(I())):
    n,d,g=map(int,I().split())
    f=1
    if(g==100 and d!=100): f=0
    if(g==0 and d!=0): f=0
    if(100//math.gcd(d,100)>n): f=0
    if(f): print(f'Case #{i+1}: Possible')
    else: print(f'Case #{i+1}: Broken')