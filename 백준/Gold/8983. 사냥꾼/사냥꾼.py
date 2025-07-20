from collections import deque as d
import sys
I=sys.stdin.readline
n,m,l=map(int,I().split())
s=[*map(int,I().split())]
s.sort()
q=d([tuple(map(int,I().split())) for _ in range(m)])
for i in range(n):
    a=s[i]
    for _ in range(len(q)):
        x,y=q.popleft()
        if(abs(a-x)+y>l): q.append((x,y))
print(m-len(q))