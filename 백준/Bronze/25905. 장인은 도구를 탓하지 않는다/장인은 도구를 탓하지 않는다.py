l=[float(input()) for _ in range(10)]
l.sort()
l.pop(0)
r=1
for i,e in enumerate(l):
    r*=e/(i+1)
print(r*1e9)