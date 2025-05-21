import heapq
n,t,p=map(int,input().split())
l=list(map(int,input().split()))
q=[]
s,m=0,0
for i in range(n):
    heapq.heappush(q,-l[i])
    s+=l[i]
    if(s>t-i*p): s+=heapq.heappop(q)
    m=max(m,len(q))    
print(m)