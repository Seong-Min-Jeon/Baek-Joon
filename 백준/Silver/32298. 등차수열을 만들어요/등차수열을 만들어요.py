a,b=map(int,input().split())
l=[2*b]
for _ in range(a-1): l.append(l[-1]+b)
print(*l)