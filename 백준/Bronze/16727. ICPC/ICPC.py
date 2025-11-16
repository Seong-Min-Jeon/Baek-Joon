a,b=map(int,input().split())
c,d=map(int,input().split())
if(a+d>b+c): print('Persepolis')
elif(a+d<b+c): print('Esteghlal')
else:
    if(b<d): print('Persepolis')
    elif(b>d): print('Esteghlal')
    else: print('Penalty')