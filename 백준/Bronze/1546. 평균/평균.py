c=int(input())
l=list(map(int,input().split()))
b,e=max(l),0
for i in range(c):
    e+=l[i]/b*100    
print(e/c)