a,b=map(int,input().split())
s=set()
t=set()
for _ in range(a):
    s.add(input())
for _ in range(b):
    t.add(input())
l=sorted(list(s.intersection(t)))
print(len(l))
for i in l:
    print(i)