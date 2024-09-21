a=int(input())
l=list(map(int,input().split()))
t,p=map(int,input().split())
x=0
for e in l: x+=(e-1)//t+1
print(x)
print(a//p, a-(a//p)*p)