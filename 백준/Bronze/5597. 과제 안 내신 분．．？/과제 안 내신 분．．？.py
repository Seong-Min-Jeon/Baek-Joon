l=[0]*30
for _ in range(28):
    s=int(input())
    l[s-1] = 1
print(*[i+1 for i, e in enumerate(l) if e==0])