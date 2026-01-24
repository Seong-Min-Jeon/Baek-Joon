n=int(input())
l=[*map(int,input().split())]
t=0
for i in range(n):
    if(i==0): t+=(l[i]-2)*180
    else: t+=l[i]*180
print(t)