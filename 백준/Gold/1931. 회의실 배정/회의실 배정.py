import sys
from collections import deque
I=sys.stdin.readline
l=[tuple(map(int,I().split())) for _ in range(int(I()))]
l.sort(key=lambda x: [x[1],x[0]])
d=deque(l)
c=0
while d:
    m=d.popleft()[1]
    while d and d[0][0]<m: d.popleft()
    c+=1
print(c)