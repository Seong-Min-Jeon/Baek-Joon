n=int(input())
l=[]
for i,e in enumerate([*map(int,input().split())]):
    l.append((e,i))
l.sort()
r=[0]*n
c=0
for _,i in l:
    r[i]=c
    c+=1
print(*r)