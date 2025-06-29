import bisect
import sys
I=sys.stdin.readline
n=int(I())
t=list(map(int,I().split()))
b=list(map(int,I().split()))
c=list(map(int,I().split()))
d=[0]*n
d[0]=c[0]
for i in range(1,n):
    j=bisect.bisect_left(t,t[i]-b[i])-1
    d[i]=max(d[i-1],c[i])
    if(j>=0): d[i]=max(d[i],d[j]+c[i])
print(d[-1])