import sys
I=sys.stdin.readline
l=[0,1]
t=[i**2 for i in range(1,1000)]
for i in range(2,10**6+1):
    x=0
    for e in t:
        if(i<e): break
        if(l[i-e]==0): x=1; break
    l.append(x)
for _ in range(int(I())):
    if(l[int(I())]==1): print('koosaga')
    else: print('cubelover')