def f(i):
    global s
    a.add(i); b.add(l[i])
    if(l[i] in a):
        if(a==b): s=s.union(a)
    else: f(l[i])
n=int(input())
l=[int(input()) for _ in range(n)]
l.insert(0,0)
s=set()
for i in range(1,n+1):
    a,b=set(),set()
    f(i)
print(len(s))
for e in sorted(list(s)):
    print(e)