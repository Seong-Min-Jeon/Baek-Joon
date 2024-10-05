input()
l=list(map(int,input().split()))
l.sort()
s=0
for i in range(len(l)):
    l[i]+=s
    s=l[i]
print(sum(l))