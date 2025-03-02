import heapq
n,m=map(int,input().split())
c=list(map(int,input().split()))
w=list(map(int,input().split()))
for i in range(n): c[i]*=-1
heapq.heapify(c)
for i in range(m):
    p=heapq.heappop(c)*-1
    if(p<w[i]): print(0); exit()
    heapq.heappush(c,(p-w[i])*-1)
print(1)