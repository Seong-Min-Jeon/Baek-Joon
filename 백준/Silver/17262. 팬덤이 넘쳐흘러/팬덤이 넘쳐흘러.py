import sys
I=sys.stdin.readline
n=int(I())
l=[tuple(map(int,I().split())) for _ in range(n)]
print(max(0,sorted(l,reverse=True)[0][0]-sorted(l,key=lambda x:x[1])[0][1]))