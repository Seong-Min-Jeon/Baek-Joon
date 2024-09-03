input()
l=list(map(int,input().split()))
m,t=0,0
for i in l:
    if(t<i): m=max(m,i-t)
    t+=i
print(m)