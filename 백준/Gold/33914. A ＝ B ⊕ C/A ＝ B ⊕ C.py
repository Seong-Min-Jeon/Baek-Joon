import math
x,y=map(int,input().split())
M=1000000007
n=(x+y)//3
c=0
while x!=2*y:
    c+=1; y-=3
    if(y<0): print(0); exit()
print((pow(3,x//2,M)*math.comb(n,c))%M)