I=input
for _ in range(int(I())):
    a,b=I().strip().split()
    b=int(b)
    t=(b%8+b//8)%2!=0
    if(b%8==0): t=not t
    if((ord(a[0])+int(a[1]))%2!=t): print('YES')
    else: print('NO')