k,l=map(int,input().split())
x=1
for i in range(2,l):
    if(k%i==0): x=i; break
if(x==1): print('GOOD')
else: print(f'BAD {x}')