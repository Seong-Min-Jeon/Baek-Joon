from collections import deque as Q
input()
l=Q(sorted([*map(int,input().split())]))
a,b=0,0
while l:
    if(len(l)%2==0):a+=l.pop()
    else:b+=l.popleft()
    if(a<=b): print('Bob'); exit()
print('Alice')