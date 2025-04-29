n,m=set(),set()
for _ in range(int(input())):
    a,b=map(int,input().split())
    n.add(a+b); m.add(a-b)
print(max(abs(max(n)-min(n)),abs(max(m)-min(m))))