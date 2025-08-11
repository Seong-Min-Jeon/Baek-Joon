import bisect
l=[1,2]
for _ in range(478): l.append(l[-1]+l[-2])
while True:
    x,y=map(int,input().split())
    if(x==y==0): break
    print(bisect.bisect_right(l,y)-bisect.bisect_left(l,x))