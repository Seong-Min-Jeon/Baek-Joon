t=int(input())
u=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    u+=a*b
if(t==u): print("Yes")
else: print("No")