import sys, heapq
I=sys.stdin.readline
for _ in range(int(I())):
    m=int(I())
    print(m//2+1)
    l=[]
    for _ in range((m-1)//10+1):
        l+=[*map(int,I().split())]
    r=[]
    p,q=[10**99],[10**99]
    for i,e in enumerate(l):
        if(-p[0]<e):
            heapq.heappush(q,e)
        else:
            heapq.heappush(p,-e)
        if(len(p)>len(q)):
            heapq.heappush(q,-heapq.heappop(p))
        elif(len(q)>len(p)+1):
            heapq.heappush(p,-heapq.heappop(q))
        if(i%2==0): r.append(q[0])
    r.reverse()
    x=[]
    t=[]
    while r:
        t.append(r.pop())
        if(len(t)==10):
            x.append(t)
            t=[]
    if(t): x.append(t)
    for e in x:
        print(*e)