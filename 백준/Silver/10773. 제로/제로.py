import sys
i=sys.stdin.readline
l=[]
for _ in range(int(i())):
    a=int(i())
    if(a==0): l.pop()
    else: l.append(a)
print(sum(l))