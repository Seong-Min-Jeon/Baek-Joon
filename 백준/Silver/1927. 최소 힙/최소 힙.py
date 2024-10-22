import sys
import heapq
i=sys.stdin.readline
l=[]
for _ in range(int(i())):
    a=int(i())
    if(a==0):
        if(len(l)==0): print(0)
        else: print(heapq.heappop(l))
    else: heapq.heappush(l,a)    