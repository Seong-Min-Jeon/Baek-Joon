s=set([])
for _ in range(10):
    i=int(input())
    s.add(i%42)
print(len(s))