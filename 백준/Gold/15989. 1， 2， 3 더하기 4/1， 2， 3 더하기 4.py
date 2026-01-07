import sys
I=sys.stdin.readline
l=[[0]*3 for _ in range(10001)]
l[1]=[1,0,0]
l[2]=[1,1,0]
l[3]=[1,1,1]
for i in range(4,10001):
    l[i][0]=l[i-1][0]
    l[i][1]=l[i-2][0]+l[i-2][1]
    l[i][2]=l[i-3][0]+l[i-3][1]+l[i-3][2]
for _ in range(int(I())):
    n=int(I())
    print(sum(l[n]))