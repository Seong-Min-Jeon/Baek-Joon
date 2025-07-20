from bisect import bisect_left as l
import sys
I=sys.stdin.readline
n,m,b=map(int,I().split())
s=[*map(int,I().split())]
q=[[*map(int,I().split())] for _ in range(m)]
s.sort(); q.sort()
c=0
for i in range(m):
    x,y=q[i]
    j=l(s,x)
    if(j>0 and abs(s[j-1]-x)+y<=b): c+=1
    elif(j<n and abs(s[j]-x)+y<=b): c+=1
print(c)