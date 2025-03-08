import heapq
n,m=map(int,input().split())
l=list(map(int,input().split()))
heapq.heapify(l)
for _ in range(m):
    a,b=heapq.heappop(l),heapq.heappop(l)
    for _ in range(2): heapq.heappush(l,a+b)
print(sum(l))