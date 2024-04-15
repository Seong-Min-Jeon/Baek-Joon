s=set()
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            s.add((a,b))
print(len(s))