import heapq
n,m,k=map(int,input().split())
q=[-int(input()) for _ in range(n)]
heapq.heapify(q)
c=[0]
while q:
    a=-heapq.heappop(q)
    if(a-m>k): heapq.heappush(q,-a+m)
    c.append(c[-1]//2+a)
c.pop(0)
print(len(c))
for e in c:
    print(e)