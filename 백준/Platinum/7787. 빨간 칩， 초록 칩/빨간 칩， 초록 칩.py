a,b=map(int,input().split())
while a%2==b%2==0: a//=2;b//=2
if(a%2==b%2): print('B player wins')
else: print('A player wins')