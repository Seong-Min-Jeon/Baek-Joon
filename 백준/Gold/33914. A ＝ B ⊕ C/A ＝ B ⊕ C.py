import math
x,y=map(int,input().split())
c,n,M=0,(x+y)//3,1000000007
while x!=2*y:
 c+=1;y-=3
 if(y<0):print(0);exit()
print((pow(3,x//2,M)*math.comb(n,c))%M)